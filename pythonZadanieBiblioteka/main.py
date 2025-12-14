from library import Book, Library

def main():
    library = Library()
    library.load_from_file("library_data.json")

    while True:
        print("\n--- MENU ---")
        print("1. Dodaj książkę")
        print("2. Wyświetl książki")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Szukaj książki")
        print("6. Zapisz i wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok wydania: ")
            library.add_book(Book(title, author, year))
            print("Książka dodana.")

        elif choice == "2":
            print("\nLista książek:")
            print(library.list_books())

        elif choice == "3":
            title = input("Podaj tytuł książki do wypożyczenia: ")
            print(library.borrow_book(title))

        elif choice == "4":
            title = input("Podaj tytuł książki do zwrotu: ")
            print(library.return_book(title))

        elif choice == "5":
            keyword = input("Podaj tytuł lub autora: ")
            print(library.search_books(keyword))

        elif choice == "6":
            library.save_to_file("library_data.json")
            print("Stan biblioteki zapisany. Do zobaczenia!")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()