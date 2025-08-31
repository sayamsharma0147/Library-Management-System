# Book class
class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.available_copies}")


# Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available_copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("Library Books:")
        for book in self.books:
            book.display_info()

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member_by_name(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None


# ====== Menu-Driven Program ======
def main():
    library = Library()
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Member Borrowed Books")
        print("6. Display All Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = len(library.members) + 1
            member = Member(name, member_id)
            library.add_member(member)

        elif choice == "3":
            member_name = input("Enter your name: ")
            member = library.find_member_by_name(member_name)
            if not member:
                print("Member not found. Please register first.")
                continue
            book_title = input("Enter book title to borrow: ")
            book = library.find_book_by_title(book_title)
            if not book:
                print("Book not found.")
                continue
            member.borrow_book(book)

        elif choice == "4":
            member_name = input("Enter your name: ")
            member = library.find_member_by_name(member_name)
            if not member:
                print("Member not found.")
                continue
            book_title = input("Enter book title to return: ")
            book = library.find_book_by_title(book_title)
            if not book:
                print("Book not found.")
                continue
            member.return_book(book)

        elif choice == "5":
            member_name = input("Enter member name: ")
            member = library.find_member_by_name(member_name)
            if not member:
                print("Member not found.")
                continue
            member.view_borrowed_books()

        elif choice == "6":
            library.display_books()

        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
