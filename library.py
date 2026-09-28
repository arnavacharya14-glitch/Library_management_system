
books = []
next_book_id = 1
loans = []
count = 1

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
        book_id = int(input("Book ID: "))
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

def issue_book(bid, mid, mem_list, dt):
    global count
    
    bk = get_book(bid)
    if bk is None:
        print("Error: Book ID not found.")
        return

    m = mem_list.get_member(mid)
    if m is None:
        print("Error: Member ID not found.")
        return

    for x in loans:
        if x["book_id"] == bid:
            print(f"Error: '{bk['name']}' is already loaned out.")
            return

    res = {
        "issue_id": count,
        "book_id": bid,
        "book_name": bk["name"],
        "author": bk["author"],
        "member_id": mid,
        "member_name": m["name"],
        "issue_date": dt
    }
    
    loans.append(res)
    print(f"Success: Book issued! Assigned transaction ID: {count}")
    count += 1

def return_book(r_id):
    for x in loans:
        if x["issue_id"] == r_id:
            loans.remove(x)
            print("Success: Book returned safely.")
            return
            
    print("Error: No active loan found with that Issue ID.")
