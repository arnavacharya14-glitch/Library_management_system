
books = []
next_book_id = 1


def add_book():
    global next_book_id
    name = input("Enter Book name: ")
    author = input("Author Name: ")
    book = {
        "id": next_book_id,
        "name": name,
        "author": author
    }
    books.append(book)
    print("Assigned book ID:", next_book_id)
    next_book_id += 1

def remove_book():
    try:
        book_id = int(input("Book ID to remove: "))
    except ValueError:
        print("Please enter a valid Book ID.")
        return
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book is removed.")
            return
    print("Book does not exist.")

def search_book():
    search = input("Book Name: ").strip().lower()
    found = False
    for book in books:
        if search in book["name"].lower():
            print(f"Name: {book['name']} | Author: {book['author']} | Book ID: {book['id']}")
            found = True
    if not found:
        print("No books found.")

def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

