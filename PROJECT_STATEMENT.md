# Project Statement

## Project Title

**Library Management System**

## 1. Introduction

A library contains a large number of books and members. Managing book records, member information, book issues, and returns manually can be time-consuming and difficult.

The **Library Management System** is a simple Python-based console application designed to perform basic library operations efficiently. It provides a menu-driven interface through which a user can manage books and members and keep track of issued books.

## 2. Problem Statement

The objective of this project is to develop a simple computer-based system that can manage basic library activities such as:

- Registering library members
- Adding books
- Removing books
- Searching for books
- Issuing books
- Returning books

The system reduces the need for maintaining these basic records manually and provides a structured way to perform common library operations.

## 3. Objectives

The main objectives of the project are:

1. To create a simple library management application using Python.
2. To maintain records of books available in the library.
3. To register and identify library members using unique member IDs.
4. To issue books to registered members.
5. To record book returns using issue IDs.
6. To provide a book search facility.
7. To practice Python programming concepts such as functions, classes, lists, dictionaries, loops, and conditional statements.
8. To understand how a larger program can be divided into separate modules.

## 4. Scope of the Project

The current version focuses on basic library operations in a console environment.

### Included

- Member registration
- Book addition
- Book removal
- Book search
- Book issue
- Book return
- Unique IDs for members, books, and issues
- Modular Python program structure

### Not Included

- Online access
- Database storage
- User authentication
- Graphical interface
- Automatic due-date calculation
- Fine calculation

These features can be added in future versions.

## 5. Modules

### Module 1: main.py

This is the main program file. It displays the menu and calls the appropriate functions from other modules.

### Module 2: library.py

This module manages the library's book records.

Functions include:

- Add book
- Remove book
- Search book
- Find book by ID

### Module 3: member.py

This module manages member records.

Functions include:

- Register member
- Find member by ID
- Find member by name

### Module 4: issue.py

This module manages book issue and return operations.

Functions include:

- Issue a book
- Check book and member IDs
- Prevent issuing the same book twice
- Return a book

## 6. Data Structures Used

The project uses:

### Lists

Lists store collections of books, members, and issued-book records.

### Dictionaries

Dictionaries store information using key-value pairs.

For example:

```python
book = {
    "id": 1,
    "name": "Python Basics",
    "author": "Example Author"
}
```

## 7. Basic Algorithm

### Add Book

1. Ask for book name.
2. Ask for author name.
3. Generate a unique Book ID.
4. Store the book record.
5. Display the Book ID.

### Register Member

1. Ask for member name.
2. Ask for email.
3. Ask for phone number.
4. Generate a unique Member ID.
5. Store the member record.

### Issue Book

1. Ask for Book ID.
2. Ask for Member ID.
3. Verify that the book exists.
4. Verify that the member exists.
5. Check whether the book is already issued.
6. Store the issue record.
7. Generate an Issue ID.

### Return Book

1. Ask for Issue ID.
2. Search the issue records.
3. Remove the matching issue record.
4. Display a successful return message.

## 8. Expected Outcome

After completing the project, the user should be able to perform basic library operations through a simple command-line menu.

The project also demonstrates how a Python application can be divided into multiple modules instead of keeping all code in one file.

## 9. Future Enhancements

Possible improvements include:

- SQLite or MySQL database
- Login and authentication
- Student and librarian roles
- Due dates
- Automatic fine calculation
- Graphical user interface
- Book categories
- Multiple copies of the same book
- Persistent data storage
- Reports for issued and available books

## 10. Conclusion

The Library Management System is a beginner-friendly Python project that demonstrates practical use of programming fundamentals. It provides a foundation that can later be expanded into a complete library management application with database storage and a graphical user interface.
