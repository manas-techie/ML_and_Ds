class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"
    
    def __repr__(self):
        return f"(title={self.title}, pages={self.pages})"
    def __len__(self):
        return self.pages


my_book = Book("Python 101", 350)

print(my_book)          # Uses __str__ -> Book: 'Python 101'
print(repr(my_book))    # Uses __repr__ -> Book(title='Python 101', pages=350)
print(len(my_book))     # Uses __len__ -> 350
