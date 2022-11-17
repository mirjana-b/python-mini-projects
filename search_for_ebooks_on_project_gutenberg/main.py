import json
from urllib.parse import quote
import os
import requests

CONNECTION_TIMEOUT = 5

class Book:
    """A class that contains author name and a title of a book.
    """

    def __init__(self, author_name, title):
        self.author_name = author_name
        self.title = title

    @classmethod
    def from_dictionary(cls, result):
        """Create object of class Book from a dictionary.

        Args:
            result (dict): A dictionary from which to create an object.

        Returns:
            object: object of Book
        """
        # TODO Handle multiple authors (example search: euclid)
        first_author = 0
        book = Book(result['authors'][first_author]['name'], result['title'])
        return book


def create_request_url():
    # TODO Do not ask for input here, but receive the query as an argument
    user_request = 'https://gutendex.com/books/?search='
    user_input = input(
        "Enter words to search author names and book titles on Project Gutenberg: ")
    user_input = quote(user_input)
    user_request += user_input
    return user_request


def print_search_results(book_objects):
    os.system("cls")
    print("Results of your search:")
    print()
    for i, result in enumerate(book_objects):
        print(f"{i+1}.")
        print(f"    Book title: {result.title}")
        print(f"    Author name: {result.author_name}")


def main():
    os.system("cls")
    # TODO Check if the response code is 200 (OK). Also check if there is already
    # a constant for that 200
    # https://requests.readthedocs.io/en/latest/api/#status-code-lookup
    response = requests.get(create_request_url(), timeout=CONNECTION_TIMEOUT).text
    json_object = json.loads(response)  # dict
    results = json_object['results']  # list of dictionaries
    # list of objects of class Book
    books = [Book.from_dictionary(result) for result in results]
    print_search_results(books)


if __name__ == "__main__":
    main()
