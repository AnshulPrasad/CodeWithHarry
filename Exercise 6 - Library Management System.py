class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_books(self, l: list):
        self.books.extend(l)
        self.no_of_books += len(l)

    def remove_books(self, l: list):
        for i in l:
            if i in self.books:
                self.books.remove(i)
                self.no_of_books -= 1

    def info(self):
        print(f"The library has {self.no_of_books} books.")
        print(f"The library has books: {self.books}")


l1 = Library()
l1.info()

l1.add_books(["book1", "book2", "book3", "book4"])
l1.info()

l1.remove_books(["book2"])
l1.info()
