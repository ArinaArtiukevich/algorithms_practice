class HeapArray:
    def __init__(self):
        self.heap = []

    def add(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def pop(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        while 2 * i + 2 < len(self.heap) and (
                self.heap[i] > self.heap[2 * i + 1] or self.heap[i] > self.heap[2 * i + 2]):
            if self.heap[2 * i + 1] < self.heap[2 * i + 2]:
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            else:
                self.heap[i], self.heap[2 * i + 2] = self.heap[2 * i + 2], self.heap[i]
                i = 2 * i + 2
        if 2 * i + 1 < len(self.heap) and self.heap[i] > self.heap[2 * i + 1]:
            self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]


if __name__ == '__main__':
    heap = HeapArray()
    heap.add(2)
    heap.add(5)
    heap.add(4)
    heap.add(11)
    heap.add(6)
    heap.add(8)
    heap.add(25)
    heap.add(12)
    heap.add(20)
    print(heap.heap)
    heap.pop()
    print(heap.heap)
