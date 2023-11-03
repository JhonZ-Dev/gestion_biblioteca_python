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
    def borrow_book(self, title, user_name):
        books_found = self.search_book(title)

        if books_found:
            available_books = [book for book in books_found if book.available]

            if available_books:
                book_to_borrow = available_books[0]
                book_to_borrow.available = False
                book_to_borrow.borrower = user_name
                return f"{book_to_borrow.title} has been borrowed by {user_name}."
            else:
                return "All copies of this book are currently unavailable."
        else:
            return "Book not found."