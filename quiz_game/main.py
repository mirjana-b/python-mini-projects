import json
import random

from game import run_game_logic

QUESTIONS_IN_QUIZ = 5
QUESTIONS_FILE = "questions.json"


class QuestionAndAnswer:
    """A class that represents a question and offered answers.
    """

    def __init__(self, question, answers, correct_index):
        self.question = question
        self.answers = answers
        self.correct_index = correct_index


def question_from_dictionary(question):
    """Create object of class QuestionAndAnswer from a dictionary.

    Args:
        question (dict): A dictionary from which to create an object.

    Returns:
        object: object of class QuestionAndAnswer
    """
    question_and_answer = QuestionAndAnswer(
        question['question'], question['answers'], question['correctIndex'])
    return question_and_answer


def select_random_questions(questions, questions_in_quiz):
    return random.sample(questions, k=questions_in_quiz)


def main():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:  # pylint: disable=invalid-name
        quiz_questions = json.load(f)
    quiz_questions = quiz_questions['questions']
    quiz_objects = [question_from_dictionary(
        question) for question in quiz_questions]

    questions_for_quiz = select_random_questions(
        quiz_objects, QUESTIONS_IN_QUIZ)

    run_game_logic(questions_for_quiz)


if __name__ == "__main__":
    main()
