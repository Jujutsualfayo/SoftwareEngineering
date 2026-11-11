class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,value):
        self.items.append(value)
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
    def peek(self):
        if not self.items:
            return None
        return self.items[0]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    
queue = Queue()

print(queue.is_empty())  # True

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())      # 3
print(queue.peek())      # 10
print(queue.dequeue())   # 10
print(queue.size())      # 2
print(queue.is_empty())  # False
        
    