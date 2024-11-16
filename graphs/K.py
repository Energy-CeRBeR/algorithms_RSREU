from collections import defaultdict

import sys

sys.setrecursionlimit(100000000)


def dfs(node):
    global time

    visited.add(node)
    d[node] = time
    time += 1

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

    f[node] = time
    time += 1


def is_parent(a, b):
    return int(d[a] < d[b] and f[b] < f[a])


n = int(input())
a = list(map(int, input().split()))

graph = defaultdict(set)
root = -1
for i in range(1, n + 1):
    if a[i - 1] == 0:
        root = i
    else:
        graph[a[i - 1]].add(i)

time = 0
d = dict()
f = dict()
visited = set()

dfs(root)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(is_parent(a, b))
