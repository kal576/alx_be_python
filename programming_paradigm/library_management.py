class Book:
    """ Book class that tracks the book, its title and availability """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    """ Represents a library with add, checkout, and returning books methods"""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
        
