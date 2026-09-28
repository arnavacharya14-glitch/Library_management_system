loans = []
count = 1

def issue_book(lib, bid, mid, mem_list, dt):
    global count
    
    bk = lib.get_book(bid)
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
