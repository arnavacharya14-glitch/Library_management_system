# Library Management System

## Project Overview

This is a simple **Library Management System** developed in Python. It is suitable as a beginner-level CSE project and can be run directly in VS Code.

The project allows a librarian/user to:

- Register library members
- Add books
- Remove books
- Search for books
- Issue books to registered members
- Return issued books
- Exit the application

## Technologies Used

- Python 3
- VS Code
- Python modules
- Lists and dictionaries
- Functions and classes
- Basic input/output and conditional statements

## Project Structure

```text
Library_Management_System/
│
├── main.py
├── library.py
├── member.py
├── issue.py
├── README.md
└── PROJECT_STATEMENT.md
```

### Description of Files

**main.py**  
Contains the main menu and connects all modules.

**library.py**  
Handles adding, removing, searching, and finding books.

**member.py**  
Handles member registration and member searching.

**issue.py**  
Handles issuing and returning books.

**README.md**  
Contains project information and instructions.

**PROJECT_STATEMENT.md**  
Contains the formal project problem statement, objectives, scope, and future enhancements.

## How to Run in VS Code

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check it using:

```bash
python --version
```

### Step 2: Open the Project

1. Extract the ZIP file.
2. Open VS Code.
3. Select **File → Open Folder**.
4. Select the `Library_Management_System` folder.

### Step 3: Run the Program

Open the VS Code terminal and type:

```bash
python main.py
```

## Menu

```text
1. Member Register
2. Book Issue
3. Book Return
4. Add Book
5. Remove Book
6. Search Book
7. Exit
```

## Example Workflow

1. Select `4` and add a book.
2. Select `1` and register a member.
3. Select `2` and enter the Book ID and Member ID.
4. Select `3` and enter the Issue ID to return the book.
5. Select `6` to search for a book.

## Important Note

This is a basic console-based project. Data is stored in memory while the program is running. When the program is closed, the data is reset.

## Future Enhancements

The project can later be upgraded with:

- File/database storage
- Login system
- Due dates and late fees
- Graphical User Interface
- Admin and student accounts
- Book availability status
- Better input validation
- SQLite/MySQL database
