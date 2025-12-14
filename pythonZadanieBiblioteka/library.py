import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"'{self.title}' wypożyczona."
        return f"'{self.title}' jest już wypożyczona."

    def return_book(self):
        self.is_available = True
        return f"'{self.title}' zwrócona."

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["title"], data["author"], data["year"])
        book.is_available = data["is_available"]
        return book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "Brak książek w bibliotece."
        result = ""
        for i, book in enumerate(self.books, 1):
            status = "Dostępna" if book.is_available else "Wypożyczona"
            result += f"{i}. {book.title} - {book.author} ({book.year}) [{status}]\n"
        return result.strip()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow_book()
        return f"Książka '{title}' nie została znaleziona."

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Książka '{title}' nie została znaleziona."

    def search_books(self, keyword):
        matches = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not matches:
            return f"Brak wyników dla '{keyword}'."
        return "\n".join([f"{book.title} - {book.author} ({book.year})" for book in matches])

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
        except FileNotFoundError:
            self.books = []