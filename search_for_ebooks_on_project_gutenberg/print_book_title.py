import os
from colorama import Fore, Style


def print_book_title(book_title, page_number, total_page_number):
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns

    page_info = "Page: " + str(page_number) + '/' + str(total_page_number)
    page_info_length = len(page_info)
    original_title_length = len(book_title)

    number_of_dots = 3
    dots = '.' * number_of_dots

    free_space_for_title = terminal_width - page_info_length - number_of_dots

    if original_title_length > free_space_for_title:
        shorter_title = book_title[:free_space_for_title]
        free_space_for_dots = terminal_width - page_info_length - len(shorter_title)
        dots = '.' * free_space_for_dots
        print(f"{Fore.GREEN}{shorter_title}{dots}{page_info}")
    elif free_space_for_title - original_title_length == number_of_dots:
        print(f"{Fore.GREEN}{book_title}{dots}{page_info}")
    elif free_space_for_title - original_title_length < number_of_dots:
        dots = '.' * (free_space_for_title - original_title_length)
        print(f"{Fore.GREEN}{book_title}{dots}{page_info}")
    elif free_space_for_title - original_title_length > number_of_dots:
        free_space_for_dots = terminal_width - page_info_length - len(book_title)
        dots = '.' * free_space_for_dots
        print(f"{Fore.GREEN}{book_title}{dots}{page_info}")

    print(f'{Fore.GREEN}_{Style.RESET_ALL}'*terminal_width)
