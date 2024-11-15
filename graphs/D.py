from collections import defaultdict


def dfs(node):
    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            dfs(v)


n, s = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))

graph = defaultdict(set)
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[i].add(j)


visited = set()
dfs(s - 1)

print(len(visited))
