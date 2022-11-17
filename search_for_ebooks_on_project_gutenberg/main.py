import json
from urllib.parse import quote
import os
import requests


class Book:
    """A class that represents author name and a title of a book.
    """

    def __init__(self, author_name, title):
        self.author_name = author_name
        self.title = title


def book(result):
    """Create object of class Book from a dictionary.

    Args:
        result (dict): A dictionary from which to create an object.

    Returns:
        object: object of Book
    """
    book_name_and_title = Book(result['authors'][0]['name'], result['title'])
    return book_name_and_title


def create_request():
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
    response = requests.get(create_request()).text
    json_object = json.loads(response)  # dict
    results = json_object['results']  # list of dictionaries
    # list of objects of class Book
    book_objects = [book(result) for result in results]
    print_search_results(book_objects)


if __name__ == "__main__":
    main()
