import random
import os
from colorama import Fore, Style

# pylint: disable = anomalous-backslash-in-string
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
# pylint: enable = anomalous-backslash-in-string


def select_country():
    europe_countries = [
        "Albania", "Andorra", "Holy See", "Austria", "United Kingdom",
        "Belarus", "Belgium", "Bulgaria", "Croatia", "Bosnia and Herzegovina",
        "Denmark", "Estonia", "Finland", "France", "Czech Republic",
        "Germany", "Greece", "Hungary", "Iceland", "Ireland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "North Macedonia", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland", "Portugal",
        "Romania", "Russia", "Serbia", "Slovakia", "Slovenia",
        "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine"
    ]

    return random.choice(europe_countries)


def letter_check(letter_guess, country_guess, country, missed_letters):
    letter_guessed = False
    for index, character in enumerate(country):
        if character.lower() == letter_guess.lower():
            country_guess[index] = character
            letter_guessed = True
    if letter_guessed is False:
        missed_letters.append(letter_guess)

    return country_guess


def print_game_starting_state():
    print("\n\n\n\n\n\n\n")


def print_hangman(missed_letters, hangman, country):
    clean_screen()
    misses_num = len(missed_letters)
    max_misses_num = len(hangman)
    if misses_num >= max_misses_num:
        print(
            f"{Fore.RED}You are hanged! The secret country was: {country}{Style.RESET_ALL}")
        print(f"{Fore.RED}{hangman[misses_num-1]}{Style.RESET_ALL}")
    else:
        hanging_process = misses_num-1
        print(f"{Fore.RED}{hangman[hanging_process]}{Style.RESET_ALL}")


def clean_screen():
    os.system('cls')


def main():
    playing = True
    country = select_country()
    country_guess = ['_']*len(country)
    missed_letters = []
    country_guess_result = ''
    starting_state = True

    clean_screen()
    while playing:
        if starting_state:
            print_game_starting_state()
            starting_state = False
        letter_guess = input(
            f"{Fore.GREEN}Enter your letter:{Style.RESET_ALL} ")

        country_guess = letter_check(
            letter_guess, country_guess, country, missed_letters)
        country_guess_result = "".join(country_guess)

        if country == country_guess_result:
            clean_screen()
            print_hangman(missed_letters, HANGMAN_PICS, country)
            print("\n\n")
            print(
                f"{Fore.GREEN}You have guessed the country, congrats!" +
                f" Secret country was {country_guess_result}.{Style.RESET_ALL}")
            playing = False
            continue
        elif len(missed_letters) >= len(HANGMAN_PICS):
            playing = False
            print_hangman(missed_letters, HANGMAN_PICS, country)
        elif len(missed_letters) == 0:
            os.system('cls')
            print_game_starting_state()
            print(
                f"{Fore.YELLOW}Your progress so far: " +
                f"{' '.join(country_guess_result)}{Style.RESET_ALL}")
        elif 0 < len(missed_letters) < len(HANGMAN_PICS):
            print_hangman(missed_letters, HANGMAN_PICS, country)
            print()
            print(
                f"{Fore.YELLOW}Your progress so far: " +
                f"{' '.join(country_guess_result)}{Style.RESET_ALL}")
            print(
                f"{Fore.RED}You have missed following letters: " +
                f"{','.join(missed_letters)}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
