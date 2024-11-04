from library_management_system.src.book_node import BookNode


class BookLinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_node = BookNode(title, author)
        new_node.next = self.head
        self.head = new_node
        print(f"Book '{title}' added to the library.")

    def remove_book(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Book '{title}' removed from the library.")
                return True
            prev = current
            current = current.next
        print(f"Book '{title}' not found in the library.")
        return False

    def find_book(self, title):
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return None

    def display_books(self):
        current = self.head
        if not current:
            print("No books in the library.")
            return
        print("Books in the library:")
        while current:
            print(f"- {current.title} by {current.author}")
            current = current.next