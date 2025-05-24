import random

# Define the Question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    ("What is the capital of France?\n(a) Berlin\n(b) Paris\n(c) Rome\nYour answer: ", "b"),
    ("What is 5 + 3?\n(a) 5\n(b) 8\n(c) 10\nYour answer: ", "b"),
    ("Which language is this quiz written in?\n(a) Java\n(b) Python\n(c) C++\nYour answer: ", "b"),
    ("Which planet is known as the Red Planet?\n(a) Mars\n(b) Venus\n(c) Jupiter\nYour answer: ", "a"),
    ("What color do you get by mixing red and white?\n(a) Pink\n(b) Purple\n(c) Orange\nYour answer: ", "a"),
]

questions = [Question(prompt, answer) for prompt, answer in question_prompts]


random.shuffle(questions)


def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1}:")
        answer = input(question.prompt).lower()
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was ({question.answer}).\n")
    print(f"You scored {score} out of {len(questions)}.")


run_quiz(questions)