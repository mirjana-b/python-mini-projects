import os
from colorama import Fore, Style


def print_book_text_in_terminal(book_text, book_title):
    terminal_size = os.get_terminal_size()
    title_length = len(book_title)
    if title_length > 69:
        terminal_height = terminal_size.lines - 4
    else:
        terminal_height = terminal_size.lines - 3
    text_lines = book_text.splitlines()
    reading = True
    current_reading_line = 0
    message_to_user = f"{Fore.GREEN}Enter(n(next page)/ p(previous page)/ " + \
        "fword (word you want to search for in printed text/ " + \
        f"q(quit))?:{Style.RESET_ALL} "
    total_page_number = len(text_lines)//terminal_height
    search_word = None
    while reading:
        page_number = current_reading_line//terminal_height + 1
        if title_length > 69:
            print(f"{Fore.GREEN}Book title: {book_title}                                                                      Page: {page_number}/{total_page_number}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Book title: {book_title}               Page: {page_number}/{total_page_number}{Style.RESET_ALL}")
        print()
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
