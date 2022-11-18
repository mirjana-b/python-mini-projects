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
        if ";" in result.author_name:
            print(f"{i+1}.")
            print(f"    Book title: {result.title}")
            print(f"    Authors' names: {result.author_name}")
        else:
            print(f"{i+1}.")
            print(f"    Book title: {result.title}")
            print(f"    Author name: {result.author_name}")


def main():
    os.system("cls")
    user_query = input(
        "Enter words to search author names and book titles on Project Gutenberg: ")

    response = requests.get(create_request_url(user_query),
                            timeout=CONNECTION_TIMEOUT)

    if response.status_code == requests.codes['ok']:
        response_text = response.text
        json_object = json.loads(response_text)  # dict
        results = json_object['results']  # list of dictionaries
        # list of objects of class Book
        books = [Book.from_dictionary(result) for result in results]
        print_search_results(books)
    else:
        print("Response status code wasn't OK!")


if __name__ == "__main__":
    main()
