import json
from urllib.parse import quote
import os
import requests
from book import Book


CONNECTION_TIMEOUT = 5


def create_request_url(query):
    user_request = 'https://gutendex.com/books/?search='
    user_query = quote(query)
    user_request += user_query
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
    user_query = input(
        "Enter words to search author names and book titles on Project Gutenberg: ")
    response = requests.get(create_request_url(user_query),
                            timeout=CONNECTION_TIMEOUT).text
    json_object = json.loads(response)  # dict
    results = json_object['results']  # list of dictionaries
    # list of objects of class Book
    books = [Book.from_dictionary(result) for result in results]
    print_search_results(books)


if __name__ == "__main__":
    main()
