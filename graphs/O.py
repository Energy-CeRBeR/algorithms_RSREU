def dfs(v, color):
    global flag

    if flag:
        return

    visited[v] = color
    for u in range(1, n + 1):
        if graph[v][u]:
            if not visited[u]:
                dfs(u, 3 - color)
            elif visited[v] == visited[u]:
                flag = True


n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
flag = False

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, 1)

print("YES" if not flag else "NO")
