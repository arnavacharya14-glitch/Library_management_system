import library as lib
import member as mem

loans = []
count = 1

def issue_book_ui():
    global count
    try:
        bid = int(input("Enter Book ID to issue: "))
        mid = int(input("Enter Member ID: "))
    except ValueError:
        print("Error: IDs must be numeric integers.")
        return
        
    dt = input("Enter Issue Date (DD-MM-YYYY): ")
    
    bk = lib.get_book(bid)
    if bk is None:
        print("Error: Book ID not found.")
        return

    m = mem.find_by_id(mid)
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

def return_book_ui():
    try:
        r_id = int(input("Enter Issue ID to return: "))
    except ValueError:
        print("Error: Issue ID must be numeric.")
        return

    for x in loans:
        if x["issue_id"] == r_id:
            loans.remove(x)
            print("Success: Book returned safely.")
            return
            
    print("Error: No active loan found with that Issue ID.")
