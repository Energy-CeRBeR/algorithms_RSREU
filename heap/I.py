import heapq
from collections import deque

n, k, p = map(int, input().split())

entries = dict()
history = list()
for i in range(p):
    car = int(input())
    history.append(car)
    if car not in entries:
        entries[car] = deque([])
    entries[car].append(i)

floor = set()
garage = []
heapq.heapify(garage)

count = 0
for i in range(p):
    car = history[i]
    entries[car].popleft()

    if car not in floor:
        if len(floor) >= k:
            floor.remove(heapq.heappop(garage)[1])
        count += 1
        floor.add(car)

    if not entries[car]:
        heapq.heappush(garage, (-n, car))
    else:
        heapq.heappush(garage, (-entries[car][0], car))

print(count)
