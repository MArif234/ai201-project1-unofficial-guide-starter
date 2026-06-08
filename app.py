"""
app.py  —  Milestone 5: Gradio web interface
=============================================

This file is the USER INTERFACE. It does not contain any RAG logic itself —
all the real work (retrieve relevant chunks -> ask Groq -> return answer +
sources) lives in main.py's ask() function. This file just:
  1. takes a question typed into a web page,
  2. calls ask() to get the answer and its sources, and
  3. shows the answer and the source list back on the page.

HOW TO RUN IT:
  From the project folder, run:   python app.py
  Then open the link it prints (usually http://localhost:7860) in your browser.
"""

# Gradio is the library that builds the web page for us — no HTML/CSS needed.
import gradio as gr

# We import our end-to-end function from main.py. Because ask() is defined there
# (and main.py only runs its own demo under "if __name__ == '__main__'"), this
# import does NOT trigger that demo — it just makes ask() available to us here.
from main import ask


def handle_query(question: str):
    """
    Called every time the user submits a question.

    It runs the full pipeline via ask(), then formats the result into the two
    things the web page displays: the answer text, and a bulleted source list.
    """
    # Guard against an empty submission so we don't waste an API call.
    if not question or not question.strip():
        return "Please type a question first.", ""

    # Run the whole RAG pipeline (retrieve -> generate -> attribute).
    result = ask(question)

    # Turn the list of source filenames into a bulleted string, one per line.
    sources = "\n".join(f"• {source}" for source in result["sources"])

    # Return two values, which line up with the two output boxes below.
    return result["answer"], sources


# --- Build the web page layout ---
# gr.Blocks() lets us arrange the page. Everything inside the "with" block is
# a piece of the page (a text box, a button, etc.).
with gr.Blocks(title="Heinz Scholarship Guide") as demo:
    # A short heading so the user knows what this tool is.
    gr.Markdown(
        "# Heinz College Scholarship Guide\n"
        "Ask about scholarships and fellowships for CMU Heinz College students. "
        "Answers come only from the collected documents."
    )

    # The box where the user types their question.
    inp = gr.Textbox(label="Your question", placeholder="e.g. What full-tuition fellowships can a Heinz student get?")

    # The button they click to submit.
    btn = gr.Button("Ask")

    # The box that shows the generated answer (lines=8 makes it tall enough).
    answer = gr.Textbox(label="Answer", lines=8)

    # The box that lists which documents the answer was retrieved from.
    sources = gr.Textbox(label="Retrieved from", lines=4)

    # --- Wire up the interactions ---
    # When the button is clicked, run handle_query with the question as input,
    # and put its two return values into the answer and sources boxes.
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])

    # Also let the user just press Enter in the textbox to submit.
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])


# Launch the local web server when we run "python app.py".
if __name__ == "__main__":
    demo.launch()
