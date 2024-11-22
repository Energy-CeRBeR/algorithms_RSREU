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
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
                    if i == j and new_dist < 0:
                        return -1

    return dist


n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

result = floyd(graph, n)

if result == -1:
    print(-1)

else:
    min_dist = float('inf')
    for i in range(n):
        for j in range(n):
            if i != j:
                min_dist = min(min_dist, result[i][j])
    print(min_dist)
