class Bookshelf():
    def __init__(self, books_dict):
        self.books = books_dict

    def __getitem__(self, key):
        return self.books[key]


b1 = {"Horror": "book1", "Fiction": "book2"}
print(b1["Horror"]) # returns book1

b = Bookshelf({"Horror": "book1", "Fiction": "book2"})
print(b["Horror"]) #
