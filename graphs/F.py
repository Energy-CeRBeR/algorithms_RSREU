import sys

sys.setrecursionlimit(1000000000)


def dfs(start):
    global find
    color[start] = "Grey"
    for v in graph[start]:
        if color[v] == "White":
            dfs(v)
        elif color[v] == "Grey":
            find = True
    color[start] = "Black"


n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))

graph = {i: set() for i in range(1, n + 1)}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if data[i - 1][j - 1] == 1:
            graph[i].add(j)

find = False
for i in range(1, n + 1):
    color = ["White"] * (n + 1)
    dfs(i)

print(int(find))
