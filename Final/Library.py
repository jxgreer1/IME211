# ----------------------------------------------------
# Final Exam: Library Book Borrowing Tracker
# ----------------------------------------------------

# Dataset 1: List of books
library_books = [
    {"book_id": "B001", "title": "1984", "author": "George Orwell"},
    {"book_id": "B002", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"book_id": "B003", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"book_id": "B004", "title": "Moby Dick", "author": "Herman Melville"},
    {"book_id": "B005", "title": "Pride and Prejudice", "author": "Jane Austen"},
]

# Dataset 2: Borrowing records
borrowing_records = [
    {"book_id": "B001", "user": "Alice", "borrow_date": "2024-12-01"},
    {"book_id": "B002", "user": "Bob", "borrow_date": "2024-12-03"},
    {"book_id": "B003", "user": "Charlie", "borrow_date": "2024-12-05"},
    {"book_id": "B001", "user": "Diana", "borrow_date": "2024-12-07"},
    {"book_id": "B005", "user": "Eve", "borrow_date": "2024-12-08"},
]
i=0
# TODO 1: Calculate total number of borrowed copies for each book. Store as borrowed_count. It should be
#  a dictionary with the book title as the key and the number of borrowed copies (as an int) as the value
for borrowed_count in borrowing_records:
    #print(borrowed_count)
    borrowed = borrowed_count["book_id"]
    AmountStored = borrowed[i]

# TODO 2: Collect user input for a book to search for by its title. If the user selects a book title that is not
#  in the dataset, reprompt them until they select a book title that exists in the dataset.
while True:
    userInput=input("Please select a book to search:")
    if userInput in ["1984","To Kill a Mockingbird","The Great Gatsby","Moby Dick","Pride and Prejudice"]:
        break
    else:
        print("Not a book")

# TODO 3: Find and store the the corresponding book ID as selected_book_id.
    if userInput == ["1984"]:
        selected_book_id = "B001"
    elif userInput == ["To Kill a Mockingbird"]:
        selected_book_id = "B002"
    elif userInput == ["The Great Gatsby"]:
        selected_book_id = "B003"
    elif userInput == ["Moby Dick"]:
        selected_book_id = "B004"
    elif userInput == ["Pride and Prejudice"]:
        selected_book_id = "B005"

# TODO 4: Find all users who borrowed the selected book. Store as borrowers. It should be a list of names.
for borrowerss in borrowing_records:
    #print(borrowed_count)
    borrowers = borrowerss["user"]

# TODO 5: Neatly print the book title, total borrowed copies, and list of borrowers. If there are no borrowers,
#  print 'No one has borrowed this book.'
#  Output should be formatted as such:
#  "1984" has been borrowed 2 times.
#  Borrowers: ['Alice', 'Diana']
for BookTitle, Borrwers in library_books:
    titles = BookTitle["title"]
    print(f"{titles} has been borrowed ")