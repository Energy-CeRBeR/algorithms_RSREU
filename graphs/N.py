from collections import defaultdict


def dfs(node):
    global flag
    if node not in visited:
        flag = True
        visited.add(node)

    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            dfs(v)


n = int(input())

graph = defaultdict(set)
for i in range(1, n + 1):
    node = int(input())
    graph[node].add(i)
    graph[i].add(node)

visited = set()
count = 0
for i in range(1, n + 1):
    flag = False
    dfs(i)
    if flag:
        count += 1

print(count)
