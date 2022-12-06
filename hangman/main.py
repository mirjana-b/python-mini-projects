import random
import os
from colorama import Fore, Style


HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
         ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']


def select_country():
    europe_countries = [
        "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan",
        "Belarus", "Belgium", "Bulgaria", "Croatia", "Cyprus",
        "Denmark", "Estonia", "Finland", "France", "Georgia",
        "Germany", "Greece", "Hungary", "Iceland", "Ireland",
        "Italy", "Kazakhstan", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "North Macedonia", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland", "Portugal",
        "Romania", "Russia", "Serbia", "Slovakia", "Slovenia",
        "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine"
    ]

    return random.choice(europe_countries)


def letter_check(letter_guess, country_guess, country, missed_letters):
    guess = None
    for index, character in enumerate(country):
        if character.lower() == letter_guess.lower():
            country_guess[index] = character
            guess = "letter_guessed"
    if guess is None:
        missed_letters += letter_guess

    return country_guess, missed_letters


def print_hangman(missed_letters, hangman):
    os.system('cls')
    if len(missed_letters) >= len(hangman):
        print(f"{Fore.RED}You are hanged!{Style.RESET_ALL}")
        print()
        print(f"{Fore.RED}{hangman[len(missed_letters)-1]}{Style.RESET_ALL}")
    else:
        hanging_process = len(missed_letters)-1
        print(f"{Fore.RED}{hangman[hanging_process]}{Style.RESET_ALL}")


def main():
    playing = True
    country = select_country()
    country_guess = ['_']*len(country)
    missed_letters = ''
    country_guess_new = ''
    os.system('cls')
    while playing:
        letter_guess = input("Enter your letter: ")
        country_guess, missed_letters = letter_check(
            letter_guess, country_guess, country, missed_letters)
        country_guess_new = "".join(country_guess)
        if country == country_guess_new:
            os.system('cls')
            print(
                f"{Fore.GREEN}You have guessed the country, congrats! Secret country was {country_guess_new}.{Style.RESET_ALL}")
            playing = False
            continue
        elif len(missed_letters) >= len(HANGMAN_PICS):
            playing = False
            print_hangman(missed_letters, HANGMAN_PICS)
        elif len(missed_letters) == 0:
            os.system('cls')
            print(f"Your progress so far: {country_guess_new}")
        if 0 < len(missed_letters) < len(HANGMAN_PICS):
            print_hangman(missed_letters, HANGMAN_PICS)
            print()
            print(f"Your progress so far: {country_guess_new}")


if __name__ == "__main__":
    main()
