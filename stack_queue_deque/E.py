from collections import deque
from sys import stdin


class Deque:
    def __init__(self) -> None:
        self.deq = deque([])

    def push_back(self, n):
        self.deq.append(n)
        return "ok"

    def push_front(self, n):
        self.deq.appendleft(n)
        return "ok"

    def pop_back(self):
        if self.deq:
            return self.deq.pop()
        else:
            return "error"

    def pop_front(self):
        if self.deq:
            return self.deq.popleft()
        else:
            return "error"

    def front(self):
        if self.deq:
            return self.deq[0]
        else:
            return "error"

    def back(self):
        if self.deq:
            return self.deq[-1]
        else:
            return "error"

    def size(self):
        return len(self.deq)

    def clear(self):
        self.deq.clear()
        return "ok"


deq = Deque()

for command in stdin:
    command = command.strip().split()

    if command[0] == "push_back":
        print(deq.push_back(int(command[1])))
    if command[0] == "push_front":
        print(deq.push_front(int(command[1])))
    elif command[0] == "pop_back":
        print(deq.pop_back())
    elif command[0] == "pop_front":
        print(deq.pop_front())
    elif command[0] == "front":
        print(deq.front())
    elif command[0] == "back":
        print(deq.back())
    elif command[0] == "size":
        print(deq.size())
    elif command[0] == "clear":
        print(deq.clear())
    elif command[0] == "exit":
        print("bye")
        break
