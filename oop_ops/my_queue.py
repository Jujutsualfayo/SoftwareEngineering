from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, value):
        self.items.append(value)
    def dequeue(self):
        if not self.items:
            return
        return self.items.popleft()
    def peek(self):
        if not self.items:
            return None
        return self.items[0]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)