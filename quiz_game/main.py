import json
import random

from game import playing_the_game


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
