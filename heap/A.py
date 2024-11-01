import sys


class MaxHeap:
    def __init__(self) -> None:
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def shiftDown(self, i):
        while i * 2 <= self.size:
            j = self.maxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def extract(self):
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shiftDown(1)

        return removed


n = int(sys.stdin.readline())
max_heap = MaxHeap()
for _ in range(n):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 0:
        max_heap.insert(query[1])
    else:
        print(max_heap.extract())
