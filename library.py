class Library:
    def __init__(self):
        self.books = []
        self.next_book_id = 1

    def add_book(self):
        name = input("Enter Book name: ")
        author = input("Author Name: ")

        book = {
            "id": self.next_book_id,
            "name": name,
            "author": author
        }

        self.books.append(book)
        print("Assigned book ID:", self.next_book_id)
        self.next_book_id += 1

    def remove_book(self):
        try:
            book_id = int(input("Book ID: "))
        except ValueError:
            print("Please enter a valid Book ID.")
            return

        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                print("Book is removed.")
                return

        print("Book does not exist.")

    def search_book(self):
        search = input("Book Name: ").strip().lower()
        found = False

        for book in self.books:
            if search in book["name"].lower():
                print(
                    "Name:", book["name"],
                    "| Author:", book["author"],
                    "| Book ID:", book["id"]
                )
                found = True

        if not found:
            print("No books found.")

    def get_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None
