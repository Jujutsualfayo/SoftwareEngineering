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
    def sift_down(self,i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
    def extract_min(self):
        if not self.heap:
            raise IndexError("Extracting from empty heap")
        min_value = self.heap[0] #stored it
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:#still not empty
            self.sift_down(0)
        return min_value
    def heapify(self, numbers):
        self.heap = numbers.copy()
        n = len(self.heap)
        start = (n - 2) // 2
        for i in range(start, -1, -1):
            self.sift_down(i)
            
             
heap = MinHeap()

try:
    heap.peek()
except IndexError as e:
    print(e)                # Empty heap

heap.heap = [2, 5, 8, 10]

print(heap.peek())          # 2
print(heap.heap)            # [2, 5, 8, 10]