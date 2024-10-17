# Class for Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True
        self.borrowedBy = None

    def borrow(self, member):
        if self.isAvailable:
            self.isAvailable = False
            self.borrowedBy = member
            member.borrowedBooks.append(self)
            print(f'{self.title} has been borrowed by {member.name}')
        else:
            print(f'{self.title} is currently unavailable.')

    def return_book(self):
        if not self.isAvailable:
            member = self.borrowedBy
            self.isAvailable = True
            self.borrowedBy = None
            member.borrowedBooks.remove(self)
            print(f'{self.title} has been returned.')
        else:
            print(f'{self.title} is already available.')

# Class for Member
class Member:
    def __init__(self, memberID, name):
        self.memberID = memberID
        self.name = name
        self.borrowedBooks = []

    def borrow_book(self, book):
        book.borrow(self)

    def return_book(self, book):
        book.return_book()

# Class for Library
class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def register_member(self, member):
        self.members.append(member)
        print(f'Member "{member.name}" has been registered.')

# Example usage
library = Library("City Library", "123 Main St")

# Create books
book1 = Book("Python Programming", "John Doe", "123456789")
book2 = Book("Data Science Essentials", "Jane Smith", "987654321")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Register a member
member1 = Member(1, "Alice")
library.register_member(member1)

# Borrow a book
member1.borrow_book(book1)

# Return a book
member1.return_book(book1)
