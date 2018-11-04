from Question import Question

question_prompts = [
    "What are the three primary colors?\n(a) Blue, yellow and red\n(b) White, black and red\n(c) Red, green and yellow\n\n",
    "Who discoved one of the first antibiotics: penicillin?\n(a) Louis Pasteur\n(b) Alexander Fleming\n(c) Otto Hahn\n\n",
    "Which planet is nearest the sun?\n(a)	Mercury\n(b) Venus\n(c) Earth\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) +"/" + str(len(questions)) + " correct")

run_test(questions)

