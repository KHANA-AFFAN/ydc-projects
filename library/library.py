from colorama import Fore, Back, Style, init
import os
import pyfiglet
import re

init(autoreset=True)

terminal_width = os.get_terminal_size().columns

def fill_line(text, bg=Back.RESET, fg=Fore.RESET):
    visible_text = re.sub(r'\x1b\[[0-9;]*m', '', text)  # remove ANSI codes
    pad = terminal_width - len(visible_text)
    return bg + fg + text + ' ' * pad + Style.RESET_ALL

ascii_title = pyfiglet.figlet_format("Welcome to\nMy Library", font="slant")
for line in ascii_title.split("\n"):
    print(fill_line(line.center(terminal_width), Back.BLUE, Fore.YELLOW))
print("\n")

library = {}

def add_book():
    heading = "--- Add New Book ---"
    print(fill_line(heading, Back.GREEN, Fore.BLACK))
    book_id = input(Fore.WHITE + "Enter Book ID: ").strip()
    if book_id in library:
        print(Fore.RED + "Book ID already exists! Use a different ID.")
        return
    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity < 1:
            print(Fore.RED + "Quantity must be at least 1.")
            return
    except ValueError:
        print(Fore.RED + "Please enter a valid number for quantity.")
        return
    library[book_id] = {
        "title": title,
        "author": author,
        "quantity": quantity,
        "borrowed": 0
    }
    print(Fore.GREEN + "✅ Book added successfully!")

def display_books():
    heading = "--- 📖 Library Book List ---"
    print(fill_line(heading, Back.CYAN, Fore.BLACK))
    if not library:
        print(Fore.RED + "⚠️ No books in the library.")
        return
    header = f"{'ID':<10} | {'Title':<30} | {'Author':<25} | {'Quantity':<10} | {'Borrowed':<10}"
    print(fill_line(header, Back.BLUE, Fore.WHITE))
    line = "-" * len(header)
    print(fill_line(line, Back.BLUE, Fore.YELLOW))
    for book_id, info in library.items():
        title = info['title']
        author = info['author']
        quantity = info['quantity']
        borrowed = info['borrowed']
        row = f"{book_id:<10} | {title:<30} | {author:<25} | {quantity:<10} | {borrowed:<10}"
        print(fill_line(row, Back.RESET, Fore.WHITE))

def borrow_book():
    heading = "--- Borrow Book ---"
    print(fill_line(heading, Back.YELLOW, Fore.BLACK))
    book_id = input(Fore.WHITE + "Enter Book ID to borrow: ").strip()
    if book_id not in library:
        print(Fore.RED + f"❌ Book ID '{book_id}' not found in the library.")
        return
    if library[book_id]['quantity'] < 1:
        print(Fore.RED + f"❌ '{library[book_id]['title']}' is currently out of stock.")
        return
    library[book_id]['quantity'] -= 1
    library[book_id]['borrowed'] += 1
    print(Fore.GREEN + f"✅ You have successfully borrowed '{library[book_id]['title']}'.")

def return_book():
    heading = "--- Return Book ---"
    print(fill_line(heading, Back.MAGENTA, Fore.BLACK))
    book_id = input(Fore.WHITE + "Enter Book ID to return: ").strip()
    if book_id not in library:
        print(Fore.RED + f"❌ Book ID '{book_id}' not found in the library.")
        return
    if library[book_id]['borrowed'] < 1:
        print(Fore.RED + f"❌ No borrowed copies of '{library[book_id]['title']}' to return.")
        return
    library[book_id]['quantity'] += 1
    library[book_id]['borrowed'] -= 1
    print(Fore.GREEN + f"✅ Thank you for returning '{library[book_id]['title']}'.")

def delete_book():
    heading = "--- Delete Book ---"
    print(fill_line(heading, Back.RED, Fore.WHITE))
    book_id = input(Fore.WHITE + "Enter Book ID to delete: ").strip()
    if book_id not in library:
        print(Fore.RED + f"❌ Book ID '{book_id}' not found.")
        return
    confirm = input(Fore.YELLOW + f"Are you sure you want to delete '{library[book_id]['title']}'? (y/n): ").strip().lower()
    if confirm == 'y':
        del library[book_id]
        print(Fore.GREEN + "✅ Book deleted successfully.")
    else:
        print(Fore.CYAN + "Cancelled. Book was not deleted.")

while True:
    menu_title = pyfiglet.figlet_format("Main Menu", font="digital")
    for line in menu_title.split("\n"):
        print(fill_line(line.center(terminal_width), Back.BLUE, Fore.WHITE))
    print(Fore.YELLOW + Style.BRIGHT + "1. Add Book")
    print(Fore.CYAN + Style.BRIGHT + "2. Display Books")
    print(Fore.BLUE + Style.BRIGHT + "3. Borrow Book")
    print(Fore.MAGENTA + Style.BRIGHT + "4. Return Book")
    print(Fore.RED + Style.BRIGHT + "5. Delete Book")
    print(Fore.WHITE + Style.BRIGHT + "6. Exit\n")
    choice = input(Fore.WHITE + "Enter your choice (1-6): ")
    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        print(Fore.GREEN + "\nThank you for using My Library. Goodbye!\n")
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6.")
        