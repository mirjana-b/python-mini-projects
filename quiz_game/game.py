import os


def print_intro():
    print("Welcome to the quiz game. Some instruction before playing:")
    print("1. The game is made out of five questions.")
    print("2. You will answer only one question at a time.")
    print("3. You will get a list of potential answers to select from.")
    print("4. Good luck and please enjoy your game!")
    print()


def print_potential_answers(list_of_answers):
    print("This is the list of potential answers:")
    for i in range(0, len(list_of_answers)):
        print(f"{i+1}. {list_of_answers[i]}")


def print_questions_answered_correctly(questions):
    print("This is a list of questions that you answered correctly:")
    for i in range(0, len(questions)):
        print(f"{i+1}. {questions[i]}")


def run_game_logic(questions):
    os.system("cls")
    print_intro()

    answer = input("If you want to continue the game press c key(continue): ")
    score = 0
    questions_answered_correctly = []

    if answer == 'c':
        os.system("cls")

        for i, question in enumerate(questions):
            print(f"Your question number {i+1} is: {question.question}")
            print_potential_answers(question.answers)
            print()
            selected_answer = int(input("Select your answer: "))

            if selected_answer - 1 == question.correct_index:
                score += 1
                questions_answered_correctly.append(question.question)

            os.system("cls")

            if i == len(questions) - 1:
                print("This was your last question")

        print(f"Your score is {score}.")
        print_questions_answered_correctly(questions_answered_correctly)

    else:
        print("You selected not to play the game. Bye 🙋‍♀️")
        return
