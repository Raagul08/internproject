import sqlite3
from tkinter import *
from tkinter import messagebox, simpledialog, ttk

# Connect to the database
connector = sqlite3.connect('library.db')
cursor = connector.cursor()

# Create the table if it doesn't exist
connector.execute('''
CREATE TABLE IF NOT EXISTS Library (
    BK_NAME TEXT,
    BK_ID TEXT PRIMARY KEY NOT NULL,
    AUTHOR_NAME TEXT,
    BK_STATUS TEXT,
    CARD_ID TEXT
)
''')

# Function to add a book
def add_book():
    bk_name = simpledialog.askstring("Book Name", "Enter the book name:")
    bk_id = simpledialog.askstring("Book ID", "Enter the book ID:")
    author_name = simpledialog.askstring("Author Name", "Enter the author name:")
    bk_status = "Available"
    card_id = ""

    if bk_name and bk_id and author_name:
        cursor.execute("INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)",
                       (bk_name, bk_id, author_name, bk_status, card_id))
        connector.commit()
        messagebox.showinfo("Success", "Book added successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to search for a book
def search_book():
    bk_name = simpledialog.askstring("Search Book", "Enter the book name to search:")
    cursor.execute("SELECT * FROM Library WHERE BK_NAME=?", (bk_name,))
    book = cursor.fetchone()
    if book:
        messagebox.showinfo("Book Found", f"Book Name: {book[0]}\nBook ID: {book[1]}\nAuthor: {book[2]}\nStatus: {book[3]}")
    else:
        messagebox.showerror("Error", "Book not found!")

# Function to display all books
def display_books():
    cursor.execute("SELECT * FROM Library")
    books = cursor.fetchall()
    if books:
        display_window = Toplevel()
        display_window.title("Library Books")
        tree = ttk.Treeview(display_window, columns=("Book Name", "Book ID", "Author", "Status"), show='headings')
        tree.heading("Book Name", text="Book Name")
        tree.heading("Book ID", text="Book ID")
        tree.heading("Author", text="Author")
        tree.heading("Status", text="Status")
        tree.pack(fill=BOTH, expand=1)
        for book in books:
            tree.insert("", END, values=(book[0], book[1], book[2], book[3]))
    else:
        messagebox.showinfo("No Books", "No books in the library.")

# Main window
root = Tk()
root.title("Library Management System")
root.geometry("400x300")

# Buttons
Button(root, text="Add Book", command=add_book).pack(pady=10)
Button(root, text="Search Book", command=search_book).pack(pady=10)
Button(root, text="Display Books", command=display_books).pack(pady=10)

root.mainloop()

# Close the database connection
connector.close()
