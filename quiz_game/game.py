import os


def print_intro():
    print("Welcome to the quiz game. Some instruction before playing:")
    print("1. The game is made out of five questions.")
    print("2. You will answer only one question at a time.")
    print("3. You will get a list of potential answers to select from.")
    print("4. Good luck and please enjoy your game! 😃")
    print()


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
            print(
                f"This is the list of potential answers: {question.answers}")
            print()
            selected_answer = int(input(
                "Select your answer(write the index of your answer, index starts from 0): "))

            if selected_answer == question.correct_index:
                score += 1
                questions_answered_correctly.append(question.question)

            os.system("cls")

            if i == len(questions) - 1:
                print("This was your last question")

        print(f"Your score is {score}.")
        print(
            f"This is a list of questions that you answered correctly. {questions_answered_correctly}")

    else:
        print("You selected not to play the game. Bye 🙋‍♀️")
        return
