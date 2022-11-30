class Book:
    """A class that contains author name, title and an url for plain text of a book.
    """

    def __init__(self, author_name, title, text_plain_url):
        self.author_name = author_name
        self.title = title
        self.text_plain_url = text_plain_url

    @classmethod
    def from_dictionary(cls, result):
        """Create object of class Book from a dictionary.

        Args:
            result (dict): A dictionary from which to create an object.

        Returns:
            object: object of Book
        """
        authors_names = '; '.join(author['name']
                                  for author in result['authors'])

        for key in result['formats'].keys():
            if "text/plain" in key:
                book = Book(authors_names,
                            result['title'], result['formats'][key])
                break
        else:
            book = Book(authors_names, result['title'], None)

        return book
