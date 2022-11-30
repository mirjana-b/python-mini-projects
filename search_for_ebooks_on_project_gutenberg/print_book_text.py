import os
import math
from colorama import Fore, Style
from commands import help_commands
from print_book_title import print_book_title

def print_book_text_in_terminal(book_text, book_title):
    terminal_size = os.get_terminal_size()
    terminal_height = terminal_size.lines - 3
    text_lines = book_text.splitlines()
    reading = True
    current_reading_line = 0
    message_to_user = f"{Fore.GREEN}Enter command or help if you want to see available commands:{Style.RESET_ALL} "
    total_page_number = math.ceil(len(text_lines)/terminal_height)
    search_word = None
    while reading:
        page_number = current_reading_line//terminal_height + 1
        print_book_title(book_title, page_number, total_page_number)
        for i in range(current_reading_line, current_reading_line + terminal_height):
            if i > len(text_lines) - 1:
                print()
                continue
            if search_word:
                colored_word = f"{Fore.GREEN}{search_word}{Style.RESET_ALL}"
                line = text_lines[i].replace(search_word, colored_word)
            else:
                line = text_lines[i]
            print(line)
        search_word = None
        answer = input(message_to_user)
        if answer == 'n':
            current_reading_line = min(
                current_reading_line + terminal_height, len(text_lines))
        elif answer == 'p':
            current_reading_line = max(
                current_reading_line - terminal_height, 0)
        elif answer.startswith('f'):
            search_word = answer[1:]
        elif answer == 'help':
            help_commands()
        elif answer == 'q':
            os.system("cls")
            print()
            print(
                f"{Fore.GREEN}I hope that you enjoyed reading the book! Bye!{Style.RESET_ALL}")
            reading = False
