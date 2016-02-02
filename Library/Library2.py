# Kevin Smith
# 1-30-16
# Code Fellows 401 Code Challenge - Library

# Description:
# Use object-oriented Python to model a public library
# (w/ three classes: Library, Shelf, & Book). The library
#  should be aware of a number of distinct shelves.
# Each shelf should know what books it contains. Create methods
# to add and remove a book from a self. The library should have
# a method to report all books it contains. Note: this should *not*
# be a Django (or any other) app - just a single file with three
# classes (plus commands at the bottom showing it works) is all
# that is needed. In addition to pushing this python file to your
# Github account, please also setup a http://repl.it/languages/Python
#  (so it runs there) and enter the saved URL here.


class Library:
    def __init__(self, name):
        self.name = name
        self.shelves = []
        self.add_shelf('unshelved')

    def add_shelf(self, name):
        """Create a new shelf in the library."""
        self.shelves.append(Shelf(name, self))

    def book_list(self):
        """Print list of all books in the library separated by shelf."""
        for shelf in self.shelves:
            print('{} contains the books: {}'.format(
                shelf.name, shelf.booklist()))

    def shelflist(self):
        """Return list of all shelves in library."""
        templist = []
        for shelf in self.shelves:
            templist.append(shelf.name)
        return templist


class Shelf:
    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.books = []

    def add_book(self, book):
        """Add book to shelf."""
        self.books.append(book)

    def remove_book(self, book):
        """Remove book from shelf."""
        self.books.remove(book)

    def booklist(self):
        """Return list of all books on the shelf."""
        templist = []
        for book in self.books:
            templist.append(book.name)
        return templist


class Book:
    def __init__(self, name, isbn):
        self.name = name
        self.isbn = isbn
        self.shelf = 'unshelved'

    def put_book(self, shelf):
        """Put book on the given shelf."""
        self.shelf = shelf.name
        shelf.add_book(self)

    def take_book(self):
        """Take the book off the shelf."""
        self.shelf = 'unshelved'


def create_book(library):
    """User can create books and add them to a shelf."""
    bookname = input('Book name:')
    bookisbn = input('ISBN:')
    book = Book(bookname, bookisbn)
    bookshelf = input('Which shelf? (0 to leave off shelf)')
    flag = True
    while flag:
        try:
            book.put_book(library.shelves[int(bookshelf)])
            flag = False
        except:
            print('Enter a number 0-3:')
            bookshelf = input('Which shelf? (0 to leave off shelf)')


def move_book(name, shelf, library):
    """Remove book from 'unshelved' and puts it on named shelf."""
    book_to_put = [mybook for mybook in library.shelves[0].books
                   if mybook.name == name][0]
    library.shelves[0].remove_book(book_to_put)
    shelf.add_book(book_to_put)


def main():
    # Create a Library with three shelves
    library = Library('Gig Harbor')
    library.add_shelf('Shelf1')
    library.add_shelf('Shelf2')
    library.add_shelf('Shelf3')

    # Add some books to the shelves
    book1 = Book("War And Peace", 123456)
    book1.put_book(library.shelves[0])
    book2 = Book("Dune", 564741)
    book2.put_book(library.shelves[2])
    book3 = Book("Ender's Game", 818552)
    book3.put_book(library.shelves[1])
    book4 = Book("Tom Sawyer", 123584)
    book4.put_book(library.shelves[0])

    # Removes a book from a shelf
    library.shelves[1].remove_book(book3)

    # User created book
    create_book(library)

    # Print Library's full book list
    library.book_list()

    # Print library's unshelved book list
    print('The books that are currently not on a shelf are {}'.format(
        library.shelves[0].booklist()))

    # User places an unshelved book on a shelf
    flag = True
    while flag:
        bookname = input('Book to put on shelf: {}'.format(
            library.shelves[0].booklist()))
        shelfindex = input('Shelf? (Enter number): {}'.format(
            library.shelflist()))
        try:
            move_book(bookname, library.shelves[int(shelfindex)], library)
            flag = False
        except:
            print('Enter a shelf number (0-3) and an unshelved book:')

    # Prints out list of all books
    library.book_list()

    # Prints out list of unshelved books
    print('The books that are currently not on a shelf are {}'.format(
        library.shelves[0].booklist()))

if __name__ == '__main__':
    main()
