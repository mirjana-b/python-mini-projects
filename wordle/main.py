import os
import random
from colors import color
from loader import load_words

NUMBER_OF_TRIES = 6
WORD_LENGTH = 5

LETTER_INCORRECT = 0
LETTER_MISPLACED = 1
LETTER_CORRECT = 2


def print_game_state(guesses, results):
    status_colors = {
        LETTER_INCORRECT: "grey",
        LETTER_MISPLACED: "yellow",
        LETTER_CORRECT: "green",
    }
    os.system("cls")
    print()

    for guess, result in zip(guesses, results):
        row = " | "

        for letter, status in zip(guess, result):
            row += color(letter.upper(), fg=status_colors[status])
            row += " "

        print(row)

    for _ in range(NUMBER_OF_TRIES - len(guesses)):
        print(" |", "_ " * WORD_LENGTH)

    print()


def get_user_input(words):
    while True:
        guess = input("Enter your guess: ").lower()

        if len(guess) == WORD_LENGTH and guess in words:
            return guess

def analyze_guess(guess, target_word):
    result = []
    analyzed = ""

    for letter, target_letter in zip(guess, target_word):
        if letter not in target_word:
            result.append(LETTER_INCORRECT)
        elif letter == target_letter:
            result.append(LETTER_CORRECT)
        else:
            analyzed_count = analyzed.count(letter)
            target_count = target_word.count(letter)

            if target_count > analyzed_count:
                result.append(LETTER_MISPLACED)
            else:
                result.append(LETTER_INCORRECT)

        analyzed += letter

    return result


def main():
    words = load_words("words.txt")
    target_word = random.choice(words)
    guesses = []
    results = []

    print_game_state(guesses, results)

    for _ in range(NUMBER_OF_TRIES):
        guess = get_user_input(words)
        result = analyze_guess(guess, target_word)

        guesses.append(guess)
        results.append(result)
        print_game_state(guesses, results)

        all_correct = all(status == LETTER_CORRECT for status in result)
        if all_correct:
            print("You win!")
            return

    print("You lose!")
    print("The right word was", target_word.upper())


if __name__ == "__main__":
    main()
