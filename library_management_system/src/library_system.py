from library_management_system.src.book_linked_list import BookLinkedList
from library_management_system.src.user_queue import UserQueue


class LibrarySystem:
    def __init__(self):
        self.books = BookLinkedList()
        self.borrow_queue = UserQueue()
        self.return_queue = UserQueue()

    def borrow_book(self, user, title):
        book = self.books.find_book(title)
        if book:
            self.borrow_queue.enqueue((user, title))
            print(f"User '{user}' requested to borrow '{title}'.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def return_book(self, user, title):
        self.return_queue.enqueue((user, title))
        print(f"User '{user}' requested to return '{title}'.")

    def process_borrow_requests(self):
        while not self.borrow_queue.is_empty():
            user, title = self.borrow_queue.dequeue()
            # Assume the borrowing process is successful
            self.books.remove_book(title)
            print(f"User '{user}' borrowed '{title}'.")

    def process_return_requests(self):
        while not self.return_queue.is_empty():
            user, title = self.return_queue.dequeue()
            # Assume the returning process is successful
            # For simplicity, author is unknown during return; in real systems, we would track this
            self.books.add_book(title, "Unknown")
            print(f"User '{user}' returned '{title}'.")
