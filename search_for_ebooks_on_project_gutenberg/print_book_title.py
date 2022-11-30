import os
from colorama import Fore, Style


def print_book_title(book_title, page_number, total_page_number):
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns

    page_info = f"Page: {page_number}/{total_page_number}"
    page_info_length = len(page_info)

    number_of_dots = 3
    dots = '.' * number_of_dots

    free_space_for_title = terminal_width - page_info_length - number_of_dots

    book_title = book_title[:free_space_for_title]

    print(f"{Fore.GREEN}{book_title:.<{free_space_for_title}}{dots}{page_info}")
    print(f'{Fore.GREEN}_{Style.RESET_ALL}'*terminal_width)
