class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None

class Library:
    """A class representing a library"""
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books