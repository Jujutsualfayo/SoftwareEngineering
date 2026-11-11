class MinHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]
    def insert(self, value):
        self.heap.append(value)
heap = MinHeap()

try:
    heap.peek()
except IndexError as e:
    print(e)                # Empty heap

heap.heap = [2, 5, 8, 10]

print(heap.peek())          # 2
print(heap.heap)            # [2, 5, 8, 10]