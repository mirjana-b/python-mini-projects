import json
import random
import os


class QuestionAndAnswer:
    def __init__(self, question, answers, correctIndex):
        self.question = question
        self.answers = answers
        self.correctIndex = correctIndex


def from_quiz_questions(question):
    """This function generates object which belongs to the class QuestionAndAnswer

    Args:
        question (dict): This function expects dictionary as an argument

    Returns:
        object: object that belongs to the class QuestionAndAnswer
    """
    question_and_answer = QuestionAndAnswer(
        question['question'], question['answers'], question['correctIndex'])
    return question_and_answer


def select_random_questions(questions):
    random.shuffle(questions)
    questions_for_quiz = []

    for i in range(0, 5):
        questions_for_quiz.append(questions[i])

    return questions_for_quiz


def playing_the_game(questions):
    os.system("cls")
    print("Welcome to the quiz game. Some instruction before playing:")
    print("1. The game is made out of five questions.")
    print("2. You will answer only one question at a time.")
    print("3. You will get a list of potential answers to select from.")
    print("4. Good luck and please enjoy your game! 😃")
    print()
    answer = input("If you want to continue the game press c key(continue): ")
    score = 0
    questions_answered_correctly = []

    if answer == 'c':
        os.system("cls")

        for i in range(0, 5):
            print(f"Your question number {i+1} is: {questions[i].question}")
            print(
                f"This is the list of potential answers: {questions[i].answers}")
            print()
            selected_answer = int(input(
                "Select your answer(write the index of your answer, index starts from 0): "))

            if selected_answer == questions[i].correctIndex:
                score += 1
                questions_answered_correctly.append(questions[i].question)

            os.system("cls")

            if i == 4:
                print("This was your last question")

        print(f"Your score is {score}.")
        print(
            f"This is a list of questions that you answered correctly. {questions_answered_correctly}")

    else:
        print("You selected not to play the game. Bye 🙋‍♀️")
        return


def main():
    with open("questions.json", "r", encoding="utf-8") as f:  # pylint: disable=invalid-name
        quiz_questions = json.load(f)
    quiz_questions = quiz_questions['questions']
    quiz_objects = []

    for question in quiz_questions:
        quiz_objects.append(from_quiz_questions(question))

    questions_for_quiz = select_random_questions(quiz_objects)

    playing_the_game(questions_for_quiz)


if __name__ == "__main__":
    main()
