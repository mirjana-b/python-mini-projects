import os
from colorama import Fore
from colorama import Style


def print_book_text_in_terminal(book_text):
    terminal_size = os.get_terminal_size()
    terminal_height = terminal_size.lines - 1
    text_lines = book_text.splitlines()
    reading = True
    current_reading_line = 0
    message_to_user = "Enter(n(next page)/ p(previous page)/ " + \
        "fword (word you want to search for in printed text/ " + \
        "q(quit))?: "

    search_word = None
    while reading:
        for i in range(current_reading_line, current_reading_line + terminal_height):
            if search_word:
                colored_word = f"{Fore.GREEN}{search_word}{Style.RESET_ALL}"
                line = text_lines[i].replace(search_word, colored_word)
            else:
                line = text_lines[i]
            print(line)
        search_word = None

        answer = input(message_to_user)

        if answer == "n":
            os.system("cls")
            current_reading_line = min(
                current_reading_line + terminal_height, len(text_lines))

        elif answer == "p":
            os.system("cls")
            current_reading_line = max(
                current_reading_line - terminal_height, 0)

        elif "f" in answer:
            search_word = answer[1:]

        elif answer == "q":
            print()
            print(
                f"{Fore.GREEN}I hope that you enjoyed reading the book! Bye!{Style.RESET_ALL}")
            reading = False
