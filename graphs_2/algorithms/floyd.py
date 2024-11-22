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


n, s, t = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

result = floyd(graph, n)
print(result[s - 1][t - 1] if result[s - 1][t - 1] != float("inf") else -1)
