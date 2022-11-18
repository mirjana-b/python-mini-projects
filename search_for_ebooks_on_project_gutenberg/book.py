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
        authors_names = '; '.join(author['name'] for author in result['authors'])
        book = Book(authors_names, result['title'])
        return book
