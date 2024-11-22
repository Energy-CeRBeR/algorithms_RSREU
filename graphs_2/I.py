def floyd(graph, n):
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


n, m = map(int, input().split())

graph = list(list(-1 if i != j else 0 for i in range(n)) for j in range(n))
for _ in range(m):
    a, b, length = map(int, input().split())
    graph[a - 1][b - 1] = length
    graph[b - 1][a - 1] = length

result = floyd(graph, n)

num = 0
cur_mx = float("inf")
for i in range(n):
    mx = max(result[i])
    if mx < cur_mx:
        num = i
        cur_mx = mx

print(num + 1)
