import library as lib
import member as mem
import issue as iss
lib_sys=lib.Library()
mem_sys = mem.MemberManager()
issue_sys=iss.IssueManager(lib_sys)

while True:
    print("\n--- LIBRARY MENU ---") 
    print("[1] Register New Candidate")
    print("[2] Issue a Book")
    print("[3] Return a Book")
    print("[4] Add New Book")
    print("[5] Remove a Book")
    print("[6] Search for Book")
    print("[7] Close Program")
    
    choice = input("\nselect the type b/w (1-7): ").strip()
     if choice == "1":
        mem_sys.register_member()
    elif choice == "2":
        issue_sys.issue_book(mem_sys)
   
     elif choice=="3":
        issue_sys.return_book()
    elif choice=="4":
        lib_sys.add_book()
    elif choice=="5":
        lib_sys.remove_book()
    elif choice == "6":
        lib_sys.search_book()
    
     elif choice=="7":
        print("have a nice day")
        break
    else:
        print("Error")
