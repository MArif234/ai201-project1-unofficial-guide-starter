"""
main.py  —  Milestone 3: Document Ingestion and Chunking
=========================================================

WHAT THIS FILE DOES (in plain English):
  1. Finds every .txt file inside the "documents/" folder.
  2. Reads the text out of each file ("ingestion").
  3. Splits that text into smaller overlapping pieces called "chunks"
     using the strategy from my planning.md:
         - chunk size  = 700 characters
         - overlap     = 150 characters
  4. Prints a summary (how many chunks, average size) and shows 5
     representative chunks so I can read them and confirm they make
     sense on their own.

WHY WE CHUNK AT ALL:
  Later (Milestone 4) we turn each chunk into numbers ("embeddings") so
  the computer can find which pieces of text best match a question.
  Whole documents are too big and unfocused to match well, so we cut
  them into bite-sized, searchable pieces first.

This file does NOT do any embedding or AI yet. That comes in
Milestones 4 and 5. This is purely "load + chunk + look at the result".
"""

# ---------------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------------
# "pathlib" is Python's modern way to work with file/folder paths. It handles
# Windows backslashes vs. Mac/Linux slashes for us, so we don't have to worry
# about it. "Path" is the main tool from that library.
from pathlib import Path

# "sys" lets us talk to the system. We use it for one thing below: telling the
# Windows console to print using UTF-8 so special characters (em-dashes, curly
# quotes, etc.) never crash the program when we print a chunk.
import sys

# By default the Windows console uses an older text encoding (cp1252) that
# can't handle some characters our documents contain. This line switches the
# console output to UTF-8, which handles everything. (Safe to leave in.)
sys.stdout.reconfigure(encoding="utf-8")


# ---------------------------------------------------------------------------
# CONFIGURATION  (the knobs from my planning.md, kept in one place up top)
# ---------------------------------------------------------------------------
# Putting these here (instead of scattered through the code) means if I ever
# want to try a different chunk size, I change it in ONE place.

CHUNK_SIZE = 700      # Each chunk is up to 700 characters long (from planning.md)
CHUNK_OVERLAP = 150   # Each chunk repeats the last 150 chars of the previous one

# Where my documents live. __file__ is "this script's location", and .parent
# is the folder it sits in. So this points to the "documents" folder that is
# right next to main.py — no matter what computer this runs on.
DOCUMENTS_DIR = Path(__file__).parent / "documents"


# ---------------------------------------------------------------------------
# STEP 1: LOAD THE DOCUMENTS
# ---------------------------------------------------------------------------
def load_documents(folder: Path) -> list[dict]:
    """
    Read every .txt file in `folder` and return a list of documents.

    Each document is stored as a small dictionary so we remember WHICH file
    each piece of text came from. We will need that filename later for
    "source attribution" (telling the user where an answer came from).

    Returns something like:
        [
            {"filename": "gem_fellowship.txt", "text": "GEM Fellowship..."},
            {"filename": "heinz_fellowship.txt", "text": "Heinz College..."},
            ...
        ]
    """
    documents = []  # start with an empty list; we'll add one dict per file

    # folder.glob("*.txt") finds every file ending in .txt inside the folder.
    # sorted(...) just puts them in a predictable alphabetical order so the
    # output looks the same every time we run it.
    for txt_file in sorted(folder.glob("*.txt")):

        # Open the file and read all of its text into one big string.
        # encoding="utf-8-sig" does two things:
        #   1. reads special characters (like – or ’) correctly, and
        #   2. automatically strips the invisible "BOM" marker that some
        #      Windows editors add to the very start of a file. Without this,
        #      that hidden character can crash printing later on.
        text = txt_file.read_text(encoding="utf-8-sig")

        # .strip() removes blank space/newlines at the very start and end.
        # (You said the documents are already clean, so this is the only
        #  light "cleaning" we do — just trimming empty edges.)
        text = text.strip()

        # Skip the file if it turned out to be empty, so we don't make
        # pointless empty chunks out of it.
        if not text:
            continue

        # Save the filename + its text together so the source is never lost.
        documents.append({
            "filename": txt_file.name,   # e.g. "gem_fellowship.txt"
            "text": text,                # the full cleaned-up text
        })

    return documents


# ---------------------------------------------------------------------------
# STEP 2: CHUNK ONE DOCUMENT'S TEXT
# ---------------------------------------------------------------------------
def chunk_text(text: str, chunk_size: int = CHUNK_SIZE,
               overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Split ONE document's text into overlapping chunks.

    THE IDEA (a "sliding window"):
      Imagine sliding a 700-character-wide window across the text. We grab
      what's inside the window, then slide it forward — but NOT a full 700.
      We slide forward by (700 - 150) = 550 characters, so the last 150
      characters of one chunk reappear at the start of the next chunk.

      Why overlap? So that if an important sentence happens to land right on
      a chunk boundary, it still appears whole in at least one chunk instead
      of being split in half and lost. (This is the buffer I described in
      planning.md.)

    READABILITY TWEAK (so chunks make sense on their own):
      A raw 700-character cut can slice a word in half ("...full schol" +
      "arship..."). To avoid that, after marking the 700-char end point we
      back up to the nearest space, so each chunk ends on a WHOLE word.
      The chunk is therefore "up to" 700 chars, not exactly 700.
    """
    chunks = []          # the finished list of text chunks for this document
    start = 0            # the character index where the current chunk begins
    text_length = len(text)

    # How far we move the window forward each time. With 700 and 150 this is
    # 550. We compute it instead of hard-coding so it always stays correct if
    # I change the numbers at the top of the file.
    step = chunk_size - overlap

    # Keep slicing until our starting point reaches the end of the text.
    while start < text_length:

        # Tentative end of this chunk: start + 700 characters — but never go
        # past the actual end of the text. min(...) caps it at text_length so
        # the final chunk doesn't try to read characters that don't exist.
        end = min(start + chunk_size, text_length)

        # ----- back up to a whole word (the readability tweak) -----
        # Only do this if we are NOT already at the very end of the text
        # (no point trimming the final chunk).
        if end < text_length:
            # Look at the slice text[start:end] and find the LAST space in it.
            # rfind(" ") returns the position of that space, or -1 if none.
            last_space = text.rfind(" ", start, end)

            # If we found a space that's actually past the start, move the
            # end back to it. (The check guards against weird cases where a
            # single "word" is longer than 700 chars and has no space.)
            if last_space != -1 and last_space > start:
                end = last_space

        # Grab the actual chunk of text from start up to end, and .strip()
        # off any leading/trailing whitespace so it reads cleanly.
        chunk = text[start:end].strip()

        # Only keep non-empty chunks.
        if chunk:
            chunks.append(chunk)

        # If this chunk reached the end of the document, we're done. Stopping
        # here prevents a tiny leftover "sliver" chunk: any text shorter than
        # the overlap (150) is already fully contained in this last chunk, so
        # there's nothing new to capture.
        if end >= text_length:
            break

        # Slide the window forward by `step`. Because step (550) is smaller
        # than chunk_size (700), the next chunk overlaps the previous one by
        # ~150 characters — exactly the overlap we wanted.
        start += step

        # ----- snap the NEW start to a whole word (start-of-chunk cleanup) -----
        # After sliding forward, `start` might land in the middle of a word,
        # which would make the next chunk begin with a fragment like "h Jones".
        # We detect that case by looking at the character just BEFORE start:
        #   - if it's whitespace (a space or newline), we're already at the
        #     clean beginning of a word, so leave start where it is.
        #   - if it's a letter, we're mid-word, so we walk `start` forward
        #     until we hit whitespace — i.e., skip past the leftover fragment
        #     so the next chunk begins with a complete word instead.
        # This trims the overlap by at most one partial word (still ~150),
        # which is a fine trade for chunks that read cleanly on their own.
        if 0 < start < text_length and not text[start - 1].isspace():
            while start < text_length and not text[start].isspace():
                start += 1

    return chunks


# ---------------------------------------------------------------------------
# STEP 3: CHUNK EVERY DOCUMENT AND ATTACH ITS SOURCE
# ---------------------------------------------------------------------------
def chunk_all_documents(documents: list[dict]) -> list[dict]:
    """
    Run chunk_text() on every document, and remember where each chunk came
    from. We return a flat list of chunk dictionaries:

        [
            {"filename": "gem_fellowship.txt", "chunk_index": 0, "text": "..."},
            {"filename": "gem_fellowship.txt", "chunk_index": 1, "text": "..."},
            ...
        ]

    Keeping the filename on every chunk is important: in Milestone 5 the
    answer can say "according to gem_fellowship.txt..." because we never
    threw away which file the text came from.
    """
    all_chunks = []

    for doc in documents:
        # Split this one document into its list of text chunks.
        pieces = chunk_text(doc["text"])

        # enumerate() gives us a counter (0, 1, 2, ...) alongside each piece,
        # which we store as "chunk_index" so each chunk has a position label.
        for i, piece in enumerate(pieces):
            all_chunks.append({
                "filename": doc["filename"],
                "chunk_index": i,
                "text": piece,
            })

    return all_chunks


# ---------------------------------------------------------------------------
# STEP 4: THE MAIN PROGRAM  (this is what actually runs)
# ---------------------------------------------------------------------------
def main():
    """Run the full Milestone 3 pipeline: load -> chunk -> report -> inspect."""
    # ---- Load every document from the documents/ folder ----
    print("Loading documents from:", DOCUMENTS_DIR)
    documents = load_documents(DOCUMENTS_DIR)
    print(f"Loaded {len(documents)} documents.\n")

    # ---- Turn all of them into chunks ----
    all_chunks = chunk_all_documents(documents)
    print(f"Produced {len(all_chunks)} chunks total.")

    # ---- A quick size sanity-check ----
    # Average chunk length tells us roughly whether our 700-char target is
    # being respected. (It'll be a bit under 700 because of the word backup.)
    if all_chunks:
        lengths = [len(c["text"]) for c in all_chunks]
        average_length = sum(lengths) / len(lengths)
        print(f"Average chunk length: {average_length:.0f} characters")
        print(f"Shortest chunk: {min(lengths)} chars | Longest chunk: {max(lengths)} chars\n")

    # ---- Print 5 REPRESENTATIVE chunks to eyeball ----
    # Instead of just the first 5 (which would all come from one document),
    # we pick 5 chunks spread evenly across the whole list. That way we see
    # samples from different documents and different positions.
    print("=" * 70)
    print("5 REPRESENTATIVE CHUNKS (read these — do they make sense alone?)")
    print("=" * 70)

    total = len(all_chunks)
    # Pick 5 evenly spaced positions: e.g. if there are 50 chunks, this grabs
    # roughly chunks 0, 10, 20, 30, 40.
    sample_count = min(5, total)  # don't ask for more than we have
    for n in range(sample_count):
        index = (n * total) // sample_count   # evenly spaced index
        chunk = all_chunks[index]

        print(f"\n--- Sample {n + 1} of {sample_count} ---")
        print(f"Source file : {chunk['filename']}")
        print(f"Chunk number: {chunk['chunk_index']}")
        print(f"Length      : {len(chunk['text'])} characters")
        print("Text:")
        print(chunk["text"])
        print("-" * 70)


# This standard Python line means: "only run main() if this file is executed
# directly (python main.py), not if it's imported by another file." It's a
# common convention you'll see in almost every Python script.
if __name__ == "__main__":
    main()
