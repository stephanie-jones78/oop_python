'''
SIMPLE LIBRARY INVENTORY PROGRAM
    Creating a library inventory management program using object oriented programming in Python.
    The program should be able to:
        - add books, 
        - display a list of available books,
        - lend a book to a user, and
        - display a list of borrowed books.
'''

# defining a base class called Book, representing any book in the library
class Book:
    # initializing Book class with title and author attributes using __init__ constructor method
    def __init__(self, title, author):
        self.title = title # store the title of the book
        self.author = author # storing book author

# defininf a derivative available book class that will inherit attributes from the book class
class AvailableBook(Book):
    # using constructor method __init__ to initialize available book class by calling the base class Book constructor and setting availability
    def __init__(self, title, author):
        super().__init__(title, author) # calling the constructor of the base Book class
        self.is_available = True # setting the book available for lending

# defining a derivative borrowed book class that will inherit attributes from the book class
class BorrowedBook(Book):
    