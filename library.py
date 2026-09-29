books=[]
next_book_id=1

def add_book():
    global next_book_id
    b_name = input("Enter Book name: ")
    author_name = input("Author Name: ")
    
    book_entry = {
        "id": next_book_id,
        "name": b_name,
        "author": author_name
    }
    books.append(book_entry)
    print("Assigned book ID:", next_book_id)
    next_book_id += 1

def remove_book():
    user_input = input("Book ID to remove: ")
    if not user_input.isdigit():
        print("Please enter a valid Book ID.")
        return
    book_id=int(user_input)
    
    for item in books:
        if item["id"] == book_id:
            books.remove(item)
            print("Book is removed.")
            return
    print("Book does not exist.")

def search_book():
    query = input("Book Name: ").strip().lower()
    match_found = False
    for b in books:
        if query in b["name"].lower():
            print(f"Name: {b['name']} | Author: {b['author']} | Book ID: {b['id']}")
            match_found = True
    if match_found == False:
        print("No books found.")

def get_book(book_id):
    for item in books:
        if item["id"] == book_id:
            return item
    return None
