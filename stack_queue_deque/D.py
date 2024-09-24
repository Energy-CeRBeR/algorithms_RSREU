from collections import deque
from sys import stdin


class Queue:
    def __init__(self) -> None:
        self.queue = deque([])

    def push(self, n):
        self.queue.append(n)
        return "ok"

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "error"

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return "error"

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        return "ok"


queue = Queue()

for command in stdin:
    command = command.strip().split()

    if command[0] == "push":
        print(queue.push(int(command[1])))
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "clear":
        print(queue.clear())
    elif command[0] == "exit":
        print("bye")
        break
