"""
evaluate.py  —  Run the evaluation-plan questions through the full pipeline.

This reuses the end-to-end ask() function from main.py. For each question it
prints: the question, my EXPECTED answer (from planning.md), the system's
ACTUAL answer, and the sources it retrieved from — so I can fill in the
Evaluation Report table in README.md by direct comparison.

Run with:  python evaluate.py
"""

from main import ask

# Each item pairs a question with the expected answer from my planning.md.
# (Questions 2-5 from my Evaluation Plan.)
EVAL = [
    {
        "question": "What specific colleges or universities partner with Heinz "
                    "College at Carnegie Mellon University to receive scholarships?",
        "expected": "Albright College, Allegheny College, Austin College, Brigham "
                    "Young University, Carnegie Mellon University, Denison University, "
                    "Earlham College, Franklin & Marshall College, Grove City College, "
                    "Hollins University, Ohio Wesleyan University, Point Park "
                    "University, Saint Vincent College, Thiel College, University of "
                    "Nebraska - Lincoln (Raikes School), University of the Virgin "
                    "Islands, Washington & Jefferson College, Weber State University, "
                    "Westminster College (PA), Wilson College",
    },
    {
        "question": "Can you list the merit-based scholarships that an information "
                    "systems management student at Heinz College could win based on "
                    "their college application?",
        "expected": "Information Systems Management Program Scholarships, Pittsburgh "
                    "Regional Leaders Scholarships, American Technology Fellowships, "
                    "IT Lab: Summer Security Intensive (SSI) Program Fellowships, "
                    "Excellence in Technology Fellowships",
    },
    {
        "question": "For the What Will Be Your Trademark Scholarship essay contest, "
                    "what is the essay prompt?",
        "expected": "Consider what you will be known for when your career is over; "
                    "what your personal brand will be, how you will impact society, "
                    "and how the $2500 will help you achieve your goals. 500 words or less.",
    },
    {
        "question": "If a student were to win the Deliberative Discourse Fellowship, "
                    "how much money would they be earning?",
        "expected": "$2,000 per semester scholarship; the recipient can earn "
                    "$4,000-$6,000 per academic year for non-tuition expenses.",
    },
]


def main():
    for i, item in enumerate(EVAL, start=2):   # numbered 2-5 to match planning.md
        print("=" * 70)
        print(f"QUESTION {i}: {item['question']}")
        print("-" * 70)
        print(f"EXPECTED:\n{item['expected']}\n")

        result = ask(item["question"])

        print(f"SYSTEM ANSWER:\n{result['answer']}\n")
        print("RETRIEVED FROM:")
        for source in result["sources"]:
            print(f"  • {source}")
        print()


if __name__ == "__main__":
    main()
