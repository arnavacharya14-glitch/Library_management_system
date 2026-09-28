from library import Library
from member import MemberManager
from issue import IssueManager


def main():
    library = Library()
    members = MemberManager()
    issues = IssueManager(library)

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Member Register")
        print("2. Book Issue")
        print("3. Book Return")
        print("4. Add Book")
        print("5. Remove Book")
        print("6. Search Book")
        print("7. Exit")

        try:
            choice = int(input("Enter the type: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            members.register_member()

        elif choice == 2:
            issues.issue_book(members)

        elif choice == 3:
            issues.return_book()

        elif choice == 4:
            library.add_book()

        elif choice == 5:
            library.remove_book()

        elif choice == 6:
            library.search_book()

        elif choice == 7:
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
