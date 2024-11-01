import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)
cost = 0
while len(a) != 1:
    first = heapq.heappop(a)
    second = heapq.heappop(a)
    cost += (first + second)
    heapq.heappush(a, first + second)

print(cost / 100 * 5)
