# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

I chose scholarships that master's and information system students at Carnegie Mellon could apply to. This knowledge is really valuable because many students believe that for a master's program like this they would have to pay full price, but that's not true in a lot of cases. Scholarship information is scattered along a variety of websites, and many students spend as much time looking for scholarships as they do applying to them. My point of this project is to be able to find a lot of the scholarship information that's available for both school-related scholarships and some private scholarships in one place. This is valuable information because it could save a college student thousands of dollars when it comes to paying for their education. Just for clarification, I am specifically looking at Heinz College at Carnegie Mellon University. Heinz College is where the Master's in Information Systems Management program is housed in the university. I am generally looking at this specific program in Heinz College, specifically at Carnegie Mellon. 
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

1. GEM Fellowship (https://www.gemfellowship.org/gem-fellowship-program/)
This is a specific fellowship for master's programs. This isn't just with Carnegie Mellon, but people in the Information Systems Management program can apply to this. 

2. Heinz College Fellowship: 
https://www.heinz.cmu.edu/programs/public-policy-management-master/heinz-college-fellowships
Is a specific fellowship program that gives a full ride to a Heinz College student, so it's possible for an information systems management student to get this. 

3. ProFellow Database: 
https://www.profellow.com/fellowship/ 
Specifically lists certain fellowships that an information system student at Carnegie Mellon could potentially use to fund their education. Specifically looking at the Paragon Policy Fellowship here that was found on the database.

4. Heinz Merit-Based Scholarships: 
https://www.heinz.cmu.edu/programs/information-systems-management-master/financial-aid-and-scholarships-mism 
These are specific merit-based scholarships that an information systems management student could win right after they submit their college application. 

5. Heinz Strategic Partner Scholarships: 
https://www.heinz.cmu.edu/admissions/strategic-partner-scholarship-program 
These are scholarships a Heinz student could win if they are members of a certain partner organization that Heinz College collaborates with. 

6. What Will Be Your TradeMark Scholarship: 
https://www.mandourlaw.com/trademark-scholarship/ 
This is a private scholarship from a law firm that a MISM student could win. 

7. Sandi Fuqua Scholarship: 
https://whitleylawfirm.com/about/scholarship/ 
This is another scholarship from a law firm. 

8. Stucky Firm Scholarship: 
https://www.thestuckeyfirm.com/about-us/scholarship/ 
This is also another scholarship from a law firm. 

9. Community Service Scholarship:
https://www.awjlaw.com/scholarship/ 
This is also a scholarship from a law firm. 

10. Book Lover Scholarship: 
https://makeheadway.com/scholarship/ 
This is a scholarship specifically from Headway, but an information systems management student could win this. 

11. CMU Financial Aid Page:
https://www.cmu.edu/graduate/funding/index.html 
This is the general Carnegie Mellon financial aid page that could be helpful for an information systems management student. 

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** Chunk size is around 700 characters. It might be a little bit less or a little bit more because I gave Claude the instruction to increase it or decrease it just to complete a word so the chunk makes coherent sense. 

**Overlap:** Once again, the overlap is about 150 characters, depending on just completing that word. It might be a little bit more or less. 

**Why these choices fit your documents:** These choices fit my documents because, for the majority of these sample questions that I have, it does answer the question. There are certain questions that don't get answered as correctly because the character count isn't large enough, but for those answers specifically, I decided to just leave it because I can't have answers that are more than 3,000 characters. I feel like that's inefficient. I don't want the answers to be long paragraphs that the user has to search through, so I decided to make the executive decision to keep the chunk count around 700 characters. 

**Final chunk count:** Around 700 characters

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 via sentence-transformers, This project is looking at chunks of information so I thought this project was simple enough for this model. 

**Production tradeoff reflection:** 

The only problem that I've run into is that for some of the questions, the chunk length wasn't enough. I would try to find a model with a higher length limit. I would also see if there's some way that the model could take snippets of chunks and make them into a response rather than taking a whole chunk and pasting that. Since one of my answers also had a problem with accuracy on demoing specific tests because one of the questions forgot a scholarship, I would also see if there is a more accurate model available to answer questions. This was a relatively small issue, but I would still look at other models for that. I would also look into API-hosted models to see if they would give more accuracy with the responses. 
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** 

When it is given a question that it doesn't have the answer to, it still does grab the chunks because it's going to grab the four chunks because k=4. However, I was very explicit with my instruction where I told it to answer the question only with the information provided and do not provide any outside knowledge or invent any sort of scholarship for the question. I told it that if there's a scenario where the documents don't contain enough information, then you have to respond with "I don't have enough information on that." 

**How source attribution is surfaced in the response:**
SYSTEM_PROMPT = (
    "...Answer the question using ONLY the information in the provided documents. "
    "Do not use any outside knowledge, and do not invent scholarships, dollar "
    "amounts, eligibility rules, or deadlines.\n"
    "If the documents do not contain enough information to answer, respond with "
    "exactly: \"I don't have enough information on that.\""
)

Specifically, the question that I used that was not in the documentation was about scholarships for Stanford medical students. Specifically, my project deals with scholarships for information systems management students at Carnegie Mellon University. There's going to be no information about scholarships for medical students. What it did is that it still grabbed the chunks, because k is equal to 4. It realized that there was literally no wording about Stanford or medical students in these chunks, so it returns that I don't have any information on that. 
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

1. What is a specific full-tuition scholarship or fellowship that a Heinz Information Systems Management student could win? 
Answer: Heinz Fellowship

This was a perfectly correct answer. It specifically returned the Heinz Fellowship answer in the chunk, and it gave a proper citation. Retriever quality was relevant, and the response accuracy was accurate. 

2. What specific colleges or universities partner with Heinz College at Carnegie Mellon University to receive scholarships? 

Answer: Albright College, Allegheny College, Austin College, Brigham Young University, Carnegie Mellon University,
Denison University, Earlham College, Franklin & Marshall College, Grove City College, Hollins University, Ohio Wesleyan University, Point Park University, Saint Vincent College, Thiel College, University of Nebraska - Lincoln, Raikes School of Computer Science and Management, University of the Virgin Islands, Washington & Jefferson College, Weber State University, Westminster College (PA), Wilson College

Above is the written expected answer, and with this specific question there were a couple of issues. This question, since there was a chunk limit of 700 characters, not all the universities were in the response. It only gave an answer for some of the universities. Chunk basically stopped at the University of Nebraska, and any of the universities that were later on that list did not make the cut into the answer. Because it didn't list all of the partner universities in this response, this is slightly inaccurate. There were no hallucinations with the model, which was good. Therefore, the retrieval quality was partially relevant, and the response accuracy was partially relevant. 

3. Can you list the merit-based scholarships that an information systems management student at Heinz College could win based on their college application? 

Answer: Information Systems Management Program Scholarships, Pittsburgh Regional Leaders Scholarships, American Technology Fellowships, it lab: summer security intensive (ssi) Program Fellowships, excellence in Technology Fellowships

The expected answer is written above, and overall the retrieval quality is partially relevant and the response accuracy is also partially accurate. This question got some of the scholarships, but it missed the Pittsburgh Regional Leader Scholarship, which was one of the scholarships that was supposed to be included on this list. Chunk in this case where that scholarship was not considered to be in the k=4 parameter, so this is a slight error in its response. 

4. For the What is Your Trademark Scholarship Essay Contest, what is the essay prompt? 
Answer: We want students to consider what they will be known for when their career is over.  We want to know what your personal brand will be, how you will impact society, and how the $2500 will help you achieve your goals. Essays should be kept to 500 words or less.

For this answer, I would say that the retrieval quality is relevant and the response accuracy is also accurate. It listed out the whole prompt for the essay, which was good. The one caveat with this response is that it did include the word count that the essay is supposed to be at, but I'm going to let that go because specifically in this question it was only asking for the essay prompt and not the word count. I feel like the word count is extra information. 

5. If a student were to win the Deliberative Discourse Fellowship, how much money would they be earning? 
Answer: 
Each year, Heinz College awards an additional $2,000 per semester scholarship to the Deliberative Discourse Fellow (DDF), who will be an incoming student who exemplifies a strong commitment to fostering spaces that encourage diverse opinions and perspectives, while working towards reducing polarization. The recipient will work with Heinz College's SEE Office on the Deliberative Discourse Initiative and can earn $4,000-$6,000 per academic year to help with their non-tuition expenses. 

This question, the retrieval quality is relevant, and the response accuracy is also accurate. The answer was in the chunk that the model gave. I will add that the response was quite wordy, but it answered the question correctly, so I am considering the response and retrieval quality to be accurate. 


---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** The question where it was asking to list the partner institutions was partially incorrect. 

**What the system returned:** There was a list of about 20 partner institutions that it was supposed to list out. Because the character limit was at 700 characters, it was only able to list approximately 15 schools. Because of that, it was not giving a completely accurate response because it missed out on some partner institutions that would qualify for this question. 

**Root cause (tied to a specific pipeline stage):**
The cause was the chunking size, because the chunking size was only about 700 characters. The whole list of schools could not fit in that character limit, so this was very much in the first part of the model. 

**What you would change to fix it:**

One thing that I did think of doing was changing the chunking size to make it a lot larger, but to fit all of the school names, I would have to significantly increase the chunk size, which I did not think was relevant compared to some of the other questions. I also did have another question that already was wordy with the character limit. For this specific part, I did not decide to make that change, but if I was looking at this model specifically in the context of the last question, I would increase the chunk size so it has enough space to answer the whole question. 

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
I liked that the spec had very specific information about the amount of chunks and the amount of overlap. This really guided the beginning steps of the models, which mostly set it up for success in later steps. It also was good that I had practice questions that I could completely use to guide my model. Based on how I was answering those questions that I had in the document, I was able to make changes with instructions. 
**One way your implementation diverged from the spec, and why:**

It did not keep the chunking size to exactly 700 characters. When the code was written to chunk at 700 characters, there were some chunks that were cutting words off, and although the chunks were readable and understandable, I just wanted to clean that aspect of the project up. Depending on just to make sure that a word was complete, the chunk was slightly less than 700 characters or slightly more than 700 characters. 
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

For milestone three, I had Claude in my terminal, so I had it look at the chunking strategy section of my planning.md document. It was able to split things up into chunks, and the chunks were around 700 characters, like I wanted. What happened is that, with some of the chunks, the chunks weren't whole words because it would cut itself off at the character limit. For some of the chunks, some words were being cut off. It still somewhat made sense, but I wanted it to be cleaner. One thing I had to do was have it chunk it so it chunks at the end of a word. It's okay if the characters aren't exactly 700, but I just wanted the wording to be clear. 

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

So, for when k equals four, the amount of chunks that we look at, there were some questions that were not being completely answered:
- There was one question that wasn't being completely answered because it forgot a scholarship.
- There was one question talking about the list of partner colleges, and not all the colleges were in the answer because the character limit was 700.

For these two instances, I then had Claude change the k-value to 6 to see if we would get a better result. The result was not better, and it was just more work for the model because the k-value had increased. I made the decision to just keep the k-value at 4, and this is a limitation of the model. 
