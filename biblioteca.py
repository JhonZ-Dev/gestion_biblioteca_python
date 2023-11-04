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
        print("Book added.")

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

    def return_book(self, title, user_name):
        books_found = self.search_book(title)

        if books_found:
            borrowed_books = [book for book in books_found if not book.available and book.borrower == user_name]

            if borrowed_books:
                book_to_return = borrowed_books[0]
                book_to_return.available = True
                book_to_return.borrower = None
                return f"{book_to_return.title} has been returned by {user_name}."
            else:
                return f"You haven't borrowed '{title}' or it's currently unavailable."
        else:
            return "Book not found."

if __name__ == "__main__":
    library = Library()

    while True:
        print("Options:")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            title = input("Enter the title to search for: ")
            found_books = library.search_book(title)

            if found_books:
                print("Books found:")
                for book in found_books:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn})")
            else:
                print("No books found.")

        elif choice == "3":
            title = input("Enter the title of the book to borrow: ")
            user_name = input("Enter your name: ")
            result = library.borrow_book(title, user_name)
            print(result)

        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            user_name = input("Enter your name: ")
            result = library.return_book(title, user_name)
            print(result)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")
