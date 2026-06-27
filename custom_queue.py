import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):

        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):

        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner.
        Dequeues all items up to and including the winner.
        Returns the winner.
        """
        if self.is_empty():
            return None


        winner = random.choice(self.items)


        while not self.is_empty():
            removed = self.dequeue()
            if removed == winner:
                break

        return winner