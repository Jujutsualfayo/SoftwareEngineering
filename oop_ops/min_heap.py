class MinHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) -1)
    def sift_up(self, i):
        while i > 0:
            parent = (i -1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
heap = MinHeap()

try:
    heap.peek()
except IndexError as e:
    print(e)                # Empty heap

heap.heap = [2, 5, 8, 10]

print(heap.peek())          # 2
print(heap.heap)            # [2, 5, 8, 10]