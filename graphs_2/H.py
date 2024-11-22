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


n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = -1

result = floyd(graph, n)
for i in range(n):
    for j in range(n):
        result[i][j] = 1 if result[i][j] != float("inf") else 0

for line in result:
    print(*line)
