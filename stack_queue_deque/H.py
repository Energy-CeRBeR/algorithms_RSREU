from collections import deque


n = int(input())

left_queue = deque([])
right_queue = deque([])

for _ in range(n):
    query = input().split()

    if query[0] == "+":
        right_queue.append(query[1])
        if len(right_queue) > len(left_queue):
            left_queue.append(right_queue.popleft())

    elif query[0] == "*":
        left_queue.append(query[1])
        if len(left_queue) - len(right_queue) > 1:
            right_queue.appendleft(left_queue.pop())

    elif query[0] == "-":
        print(left_queue.popleft())
        if len(right_queue) > len(left_queue):
            left_queue.append(right_queue.popleft())
