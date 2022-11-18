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
        first_author = 0
        authors_names = ''
        number_of_authors = len(result['authors'])
        if number_of_authors > 1:
            for i, author in enumerate(result['authors']):
                if i > 0:
                    authors_names += '; '
                    authors_names += author['name']
                else:
                    authors_names += author['name']
            book = Book(authors_names, result['title'])
            return book
        else:
            book = Book(result['authors'][first_author]
                        ['name'], result['title'])
            return book
