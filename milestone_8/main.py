import json

class Book:
    def __init__(self, id, title, author, category, year_of_publishing):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.year_of_publishing = year_of_publishing

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year_of_publishing})"

class Shelf:
    def __init__(self):
        self.books = []
        self.categories = set()

    def addBook(self, book):
        self.books.append(book)
        self.categories.add(book.category)

    def sortBooks(self):
        self.books.sort(key=lambda x: x.title)

def organize_books_into_shelves(books):
    shelves = {}
    for book in books:
        if book.category not in shelves:
            shelves[book.category] = Shelf()
        shelves[book.category].addBook(book)
    return shelves

def load_books_from_json(file_path):
    with open(file_path, 'r') as file:
        books_data = json.load(file)
    books = [Book(**data) for data in books_data]
    return books

def main():
    # Load books from JSON file
    books = load_books_from_json('books.json')

    # Organizing books into shelves
    shelves = organize_books_into_shelves(books)

    # Sorting books in each shelf
    for shelf in shelves.values():
        shelf.sortBooks()

    # Printing the sorted books in each shelf
    for category, shelf in shelves.items():
        print(f"\n Shelf with categories: {category}")
        for book in shelf.books:
            print(book)

if __name__ == "__main__":
    main()
