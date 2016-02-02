

class Library:
    def __init__(self, name):
        self.name = name
        self.shelves = {}

    def add_shelf(self, shelf_name):
        self.shelves[shelf_name] = Shelf(shelf_name, self)
        return self.shelves[shelf_name]

    def book_list(self):
        booklist = []
        for shelf in self.shelves:
            booklist = booklist + shelf.books
        return booklist


class Shelf:
    def __init__(self, shelf_name, library):
        self.shelf_name = shelf_name
        self.library = library
        self.library.add_shelf(self)

        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return self.books[-1]


class Book:
    def __init__(self, name, isbn):
        self.name = name
        self.isbn = isbn
        self.shelf = 'unshelved'

    def put_book(self, shelf):
        self.shelf = shelf.name
        shelf.add_book(shelf, self)

    def take_book(self):
        self.shelf = 'unshelved'


# class shelfRunning:
#     def __init__(self, shelf, year):
#         self.shelf = shelf
#         self.year = year
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)


GHlibrary = Library('Gig Harbor')
firstshelf = Shelf('Shelf1', GHlibrary)
# mam1000w_2013 = mam1000w.add_running(2013)

book = Book("war and peace", 123456)
firstshelf.add_book(book)
