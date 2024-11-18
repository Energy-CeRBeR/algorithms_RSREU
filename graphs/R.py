import sys

sys.setrecursionlimit(100000000)


def dfs(node):
    global flag
    if node not in visited:
        flag = True
        visited.add(node)

    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            dfs(v)


m, n = map(int, input().split())
field = list(list(list(input())) for _ in range(m))


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
graph = dict()
for i in range(m):
    for j in range(n):
        if field[i][j] == "#":
            if (i, j) not in graph:
                graph[(i, j)] = set()

            for direction in directions:
                next_pos = (i + direction[0], j + direction[1])
                if 0 <= next_pos[0] < m and 0 <= next_pos[1] < n and field[next_pos[0]][next_pos[1]] == "#":
                    graph[(i, j)].add(next_pos)

visited = set()
count = 0
for i in range(m):
    for j in range(n):
        flag = False
        if field[i][j] == "#":
            dfs((i, j))
            if flag:
                count += 1

print(count)
