class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty():
            self.items.append((item, item))
        else:
            self.items.append((item, min(self.items[-1][1], item)))

    def pop(self):
        return self.items.pop()[0]

    def get_min(self):
        if self.isEmpty():
            return 10 ** 28
        return self.items[-1][1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def isEmpty(self):
        return self.left_stack.isEmpty() and self.right_stack.isEmpty()

    def push(self, item):
        self.left_stack.push(item)

    def pop(self):
        if self.right_stack.isEmpty():
            while not self.left_stack.isEmpty():
                self.right_stack.push(self.left_stack.pop())
        return self.right_stack.pop()

    def get_min(self):
        return min(self.left_stack.get_min(), self.right_stack.get_min())


n, k = map(int, input().split())
a = list(map(int, input().split()))

q = Queue()
for i in range(k):
    q.push(a[i])

print(q.get_min())

for i in range(k, n):
    q.pop()
    q.push(a[i])
    print(q.get_min())
