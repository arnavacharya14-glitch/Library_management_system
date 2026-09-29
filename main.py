import library as lib
import member as mem
import issue as iss

if __name__ == '__main__':
    while True:
        print("\n--- LIBRARY MENU ---") 
        print(" Register New Candidate")
        print(" Issue a Book")
        print(" Return a Book")
        print(" Add New Book")
        print(" Remove a Book")
        print(" Search for Book")
        print(" Close Program")
        
        choice = input("\nselect the type b/w (1-7): ")
        choice = choice.strip()
        
        if choice == "1":
            mem.add_new_user()
        elif choice == "2":
            iss.issue_book_ui()
        elif choice == "3":
            iss.return_book_ui()
        elif choice == "4":
            lib.add_book()
        elif choice == "5":
            lib.remove_book()
        elif choice == "6":
            lib.search_book()
        elif choice == "7":
            print("have a nice day")
            break
        else:
            print("Error")
