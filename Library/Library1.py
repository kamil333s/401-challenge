# Codefellows code challenge problem - Library classes
# Kevin Smith
# 1/20/16


class Book(object):
    def __init__(self, **kwargs):
        self.variables = kwargs
        # print(self.variables)

    # def set_isbn(self, num):
    #     self.variables['ISBN'] = num

    # def set_title(self, title):
    #     self.variables['Title'] = title

    # def set_variable(self, k, v):
    #     self.variables[k] = v

    # def get_variable(self, k):
    #     return self.variables.get(k, None)


class Shelf(object):
    def __init__(self, **kwargs):
        self.variables = kwargs

    def add_book(self, book):
        print('before:' + self.books)
        self.books.append(book)
        print('after:' + self.books)
        # print(book)
        # print(self._books)

    def get_name(self):
        return self.variables['name']
    # def del_book(self):
    #     pass


class Library(object):
    def __init__(self, shelfnum):
        self.shelves = []
        for i in range(1, shelfnum + 1):
            newshelfname = 'Shelf' + str(len(self.shelves))
            newshelf = Shelf(name=newshelfname)
            self.shelves.append(newshelf)

    # def __iter__(self):
    #     i = 0
    #     while i <= len(self.shelves):
    #         yield self.shelves[i]
    #         i += 1

    # self._shelves = {'unshelved': []}
    # creates a new empty shelf named 'Shelf#'
    def add_shelf(self):
        newshelfname = 'Shelf' + str(len(self.shelves))
        newshelf = Shelf(name=newshelfname)
        self.shelves.append(newshelf)

    # deletes the named shelf and all books on it
    def del_shelf(self, shelfname):
        del self.shelves[shelfname]

    # def booklist(self):
    #    for shelf in self._shelves:
    #       print shelf

    def get_shelves(self):
        return self.shelves


def main():

    ghlib = Library(5)
    ghlib.add_shelf()
    ghlib.add_shelf()
    # ghlib.del_shelf('Shelf2')
    # booktitle = input('Enter book title:')
    # booknum = input('Enter ISBN:')
    booktitle = 'War and Peace'
    booknum = '123456789'
    newbook = Book(ISBN=booknum, Title=booktitle)
    # print(newbook)
    # print(newbook.variables)
    # ghlib._shelves['unshelved'].add_book(newbook)
    # print(newbook.get_variable('ISBN'))
    # print(newbook.get_variable('Title'))
    print('Shelves:{}'.format(ghlib.get_shelves()))
    # for shelf in ghlib:
    #     print(shelf.get_name)


if __name__ == "__main__":
    main()
