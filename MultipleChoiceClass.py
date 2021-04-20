from question import Question

questions_prompts = [
    "What color are banananas? \n (a) teal \n (b) magenta \n (c) yellow \n \n"
    "What color are apples? \n (a)red/green \n (b) orange \n (c) gold \n \n"
    "What color are strawberries \n (a) yellow \n (b) red \n (c)black \n \n "
]
questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + "correct!"



run_test(questions)