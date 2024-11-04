class UserQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, user):
        self.queue.append(user)
        print(f"User '{user}' added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("No users in the queue.")
            return None
        user = self.queue.pop(0)
        print(f"User '{user}' removed from the queue.")
        return user

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
