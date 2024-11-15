from collections import defaultdict

import sys

sys.setrecursionlimit(100000000)


def dfs(node):
    if node not in visited:
        cur_visited.add(node)
        visited.add(node)

    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            dfs(v)


n, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = set()
count = 0
components = []
for i in range(1, n + 1):
    cur_visited = set()
    dfs(i)
    if cur_visited:
        components.append(cur_visited)

print(len(components))
for data in components:
    print(len(data))
    print(*data)
