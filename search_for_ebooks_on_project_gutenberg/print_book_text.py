import os
from colorama import Fore
from colorama import Style


def print_book_text_in_terminal(book_text):
    terminal_size = os.get_terminal_size()
    terminal_height = terminal_size.lines
    text_lines = book_text.splitlines()
    reading = True
    current_reading_line = 0
    while reading:
        for i in range(current_reading_line, current_reading_line + terminal_height):
            print(text_lines[i])

        current_reading_line = i
        answer = input(
            "Dp you want to continue reading(y for yes and n for no)?: ")
        if answer == "n":
            print()
            print(
                f"{Fore.GREEN}I hope that you enjoyed reading the book! Bye!{Style.RESET_ALL}")
            reading = False

    return
