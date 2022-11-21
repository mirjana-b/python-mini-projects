from urllib.parse import quote
import os
import requests
from colorama import Fore
from colorama import Style
from book import Book
from print_book_text import print_book_text_in_terminal

CONNECTION_TIMEOUT = 5


def create_request_url(query):
    user_request = 'https://gutendex.com/books/?search='
    user_query = quote(query)
    user_request += user_query
    return user_request


def print_search_results(book_objects):
    os.system("cls")
    print(f"{Fore.GREEN}Results of your search:{Style.RESET_ALL}")
    print()
    for i, result in enumerate(book_objects):
        if ";" in result.author_name:
            print(f"{i+1}.")
            print(f"    {Fore.GREEN}Book title:{Style.RESET_ALL} {result.title}")
            print(
                f"    {Fore.GREEN}Authors' names:{Style.RESET_ALL} {result.author_name}")
        else:
            print(f"{i+1}.")
            print(f"    {Fore.GREEN}Book title:{Style.RESET_ALL} {result.title}")
            print(
                f"    {Fore.GREEN}Author name:{Style.RESET_ALL} {result.author_name}")


def print_book_for_reading(index, books):
    os.system("cls")
    book_index = index - 1
    result = books[book_index]

    if result.text_plain_url is None:
        print("There is no plain text for that book")
        return

    response = requests.get(result.text_plain_url,
                            timeout=CONNECTION_TIMEOUT)
    book_text = response.text
    print_book_text_in_terminal(book_text)
    return


def main():
    os.system("cls")
    user_query = input(
        "Enter words to search author names and book titles on Project Gutenberg: ")
    response = requests.get(create_request_url(user_query),
                            timeout=CONNECTION_TIMEOUT)

    if response.status_code == requests.codes['ok']:
        json_object = response.json()
        results = json_object['results']
        books = [Book.from_dictionary(result) for result in results]

        print_search_results(books)
        print()
    else:
        print("Response status code wasn't OK!")

    message = "Would you like to read book from your search results? " + \
              "If you do, enter the number of the book: "
    answer = int(input(message))
    print_book_for_reading(answer, books)


if __name__ == "__main__":
    main()
