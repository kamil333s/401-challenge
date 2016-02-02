# Codefellows code challenge problem - Library classes
# Kevin Smith
# 1/20/16


class Library:
    def __init__(self, shelfnum):
        self._shelves = {'unshelved': []}
        for i in range(1, shelfnum + 1):
            self._shelves['Shelf' + str(i)] = []

    # creates a new empty shelf named 'Shelf#'
    def add_shelf(self):
        self._shelves['Shelf' + str(len(self._shelves))] = []

    # deletes the named shelf and all books on it
    def del_shelf(self, shelfname):
        del self._shelves[shelfname]

    # def booklist(self):
    #    for shelf in self._shelves:
    #       print shelf

    def get_shelves(self):
        return self._shelves


class Shelf(Library):
    def __init__(self, **kwargs):
        self.variables = kwargs
        print('Shelf made!')

    def add_book(self, book):
        pass
        # print(book)
        # print(self._books)

    def del_book(self):
        pass


class Book():
    def __init__(self, **kwargs):
        self.variables = kwargs
        # print(self.variables)
        super().add_book(kwargs)

    # def set_isbn(self, num):
    #     self.variables['ISBN'] = num

    # def set_title(self, title):
    #     self.variables['Title'] = title

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():

    ghlib = Library(5)
    ghlib.add_shelf()
    ghlib.del_shelf('Shelf2')
    # booktitle = input('Enter book title:')
    # booknum = input('Enter ISBN:')
    # booktitle = 'War and Peace'
    # booknum = '123456789'
    # newbook = Book(ISBN=booknum, Title=booktitle)
    # print(newbook.get_variable('ISBN'))
    # print(newbook.get_variable('Title'))
    print('Shelves:{}'.format(ghlib.get_shelves()))


if __name__ == "__main__":
    main()
