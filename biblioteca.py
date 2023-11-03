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