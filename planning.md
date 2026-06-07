# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

I chose scholarships that master's and information system students at Carnegie Mellon could apply to. This knowledge is really valuable because many students believe that for a master's program like this they would have to pay full price, but that's not true in a lot of cases. Scholarship information is scattered along a variety of websites, and many students spend as much time looking for scholarships as they do applying to them. My point of this project is to be able to find a lot of the scholarship information that's available for both school-related scholarships and some private scholarships in one place. This is valuable information because it could save a college student thousands of dollars when it comes to paying for their education. Just for clarification, I am specifically looking at Heinz College at Carnegie Mellon University. Heinz College is where the Master's in Information Systems Management program is housed in the university. I am generally looking at this specific program in Heinz College, specifically at Carnegie Mellon. 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
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
Specifically lists certain fellowships that an information system student at Carnegie Mellon could potentially use to fund their education. 

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** I am thinking the chunk size should be around 700 characters. 

**Overlap:** I think the overlap size should be around 150 characters. 

**Reasoning:** The majority of the information about the scholarships and fellowships is in paragraph form. Some paragraphs are more on the lengthy side, so I chose 700 characters to make sure the information doesn't get cut off while the explanation is happening. For example, if someone asks about the criteria for applying and the criteria is long, I don't want that to cut off. The overlap size is just there in case something doesn't make grammatical sense and we need to go further into the beginning of the sentence, or if information gets cut off about eligibility criteria or something, just so we have a 150-character buffer. 

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2 via sentence-transformers

**Top-k:** k = 4

**Production tradeoff reflection:** I am just going to use the suggested model, and the reason why I'm choosing k = 4 is because, with the chunks, I kind of want to make sure that it hits all the parts of the scholarship if someone asks about it. I want the context to be lengthy enough so that it answers the person's question because I'm worried about that due to everything being in paragraph form. If the model has about four chunks to look at before generating the answer, I feel like that should be enough information for the scholarship, considering the fact that the majority of the things are in paragraph form or bullet point form. The trade-offs that I'll be weighing are based on the wording of the scholarship, The model might not be able to pick up the difference between a fellowship and a scholarship, so it might give mixed information. I am also a little bit worried about it giving too much information. Someone might just ask it to list some scholarships they can apply to, and it might start to give full explanations. I'm not really sure. 

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

1. What is a specific full-tuition scholarship or fellowship that a Heinz Information Systems Management student could win? 
Answer: Heinz Fellowship

2. What specific colleges or universities partner with Heinz College at Carnegie Mellon University to receive scholarships? 

Answer: Albright College, Allegheny College, Austin College, Brigham Young University, Carnegie Mellon University,
Denison University, Earlham College, Franklin & Marshall College, Grove City College, Hollins University, Ohio Wesleyan University, Point Park University, Saint Vincent College, Thiel College, University of Nebraska - Lincoln, Raikes School of Computer Science and Management, University of the Virgin Islands, Washington & Jefferson College, Weber State University, Westminster College (PA), Wilson College

3. Can you list the merit-based scholarships that an information systems management student at Heinz College could win based on their college application? 

Answer: Information Systems Management Program Scholarships, Pittsburgh Regional Leaders Scholarships, American Technology Fellowships, it lab: summer security intensive (ssi) Program Fellowships, excellence in Technology Fellowships

4. For the What is Your Trademark Scholarship Essay Contest, what is the essay prompt? 
Answer: We want students to consider what they will be known for when their career is over.  We want to know what your personal brand will be, how you will impact society, and how the $2500 will help you achieve your goals. Essays should be kept to 500 words or less.

5. If a student were to win the Deliberative Discourse Fellowship, how much money would they be earning? 
Answer: 
Each year, Heinz College awards an additional $2,000 per semester scholarship to the Deliberative Discourse Fellow (DDF), who will be an incoming student who exemplifies a strong commitment to fostering spaces that encourage diverse opinions and perspectives, while working towards reducing polarization. The recipient will work with Heinz College's SEE Office on the Deliberative Discourse Initiative and can earn $4,000-$6,000 per academic year to help with their non-tuition expenses. 
---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The chunking of the answers might end up giving not enough information to answer the question, which could lead to inaccurate answers. 

2. The documents could be, since some of them are formatted in bullet points and some of them are formatted in long paragraph format. It might not be able to chunk or overlap the information correctly. 

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

     [Scholarship .txt files] → [Information Chunked into 700-character pieces with 150-character overlap] → [all-MiniLM-L6-v2 + ChromaDB used] → [Relevant scholarship chunks found] → [Groq llama-3.3-70b generates answer to user's prompt]

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:** I'll be using Claude to create a script that would take the 10 or 11 TXT files of the scholarship information with my .md file and it would split that up into the 700-character chunks. I will be implementing chunk_text() so I will ask Claude to implement that. I then will actually print out the chunks to see if they're actually 700 characters long. 

**Milestone 4 — Embedding and retrieval:** 
For milestone four, I will be using Claude. I will give it my MD file, specifically the retrieval approach part of it, and I will also give it the pipeline diagram that I made. Claude will be able to generate a Python script that takes those chunks and stores them in the chroma b database. It'll have some sort of function that returns relevant chunks based on the question that's being asked. To check that this is working, I will take some of the test questions that I made, and I'll see what chunks get printed when I ask them to make sure that it's talking about the correct things. 
**Milestone 5 — Generation and interface:**
I'll be using Claude for this milestone. Giving it the.md file, and I will tell it to take those trunks and run them through grok to see what answers will be coming out. I'll try to ask it questions that aren't as relevant to the documents that I gave it, to make sure that it's either giving the correct answer or that it actually just says it doesn't have enough information to answer the question, rather than hallucinating. 