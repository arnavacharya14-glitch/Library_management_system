class IssueManager:
    def __init__(self, library):
        self.library = library
        self.issued_books = []
        self.next_issue_id = 1

    def issue_book(self, members):
        if not self.library.books:
            print("No books are available in the library.")
            return

        try:
            book_id = int(input("Book ID: "))
            member_id = int(input("Member ID: "))
        except ValueError:
            print("Please enter valid numeric IDs.")
            return

        book = self.library.get_book(book_id)
        member = members.get_member(member_id)

        if book is None:
            print("Book ID not found.")
            return

        if member is None:
            print("Member ID not found.")
            return

        for issued in self.issued_books:
            if issued["book_id"] == book_id:
                print("This book is already issued.")
                return

        issue_date = input("Issue date: ")

        issued = {
            "issue_id": self.next_issue_id,
            "book_id": book_id,
            "book_name": book["name"],
            "author": book["author"],
            "member_id": member_id,
            "member_name": member["name"],
            "issue_date": issue_date
        }

        self.issued_books.append(issued)

        print("Assigned issue ID:", self.next_issue_id)
        self.next_issue_id += 1

    def return_book(self):
        try:
            issue_id = int(input("Issue ID: "))
        except ValueError:
            print("Please enter a valid Issue ID.")
            return

        for issued in self.issued_books:
            if issued["issue_id"] == issue_id:
                self.issued_books.remove(issued)
                print("Book returned successfully.")
                return

        print("Issue ID not found.")
