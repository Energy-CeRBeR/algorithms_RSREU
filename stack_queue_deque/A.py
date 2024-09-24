from sys import stdin


class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def push(self, num):
        self.stack.append(num)
        return "ok"

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "error"

    def back(self):
        if self.stack:
            return self.stack[-1]
        return "error"

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        return "ok"


stack = Stack()

for command in stdin:
    command = command.strip().split()

    if command[0] == "push":
        print(stack.push(int(command[1])))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "back":
        print(stack.back())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "clear":
        print(stack.clear())
    elif command[0] == "exit":
        print("bye")
        break
