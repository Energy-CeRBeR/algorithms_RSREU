import heapq


def dijkstra(graph, start, end):
    pq = []

    dist = {node: INF for node in graph}
    dist[start] = 0

    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_vertex == end:
            return dist[end]

        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex]:
            d = cur_dist + weight
            if d < dist[neighbor]:
                dist[neighbor] = d
                heapq.heappush(pq, (d, neighbor))

    return -1


INF = 10 ** 10

n, s, f = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

graph = {i: set() for i in range(n)}
for i in range(n):
    for j in range(n):
        if a[i][j] != -1 and i != j:
            graph[i].add((j, a[i][j]))

print(dijkstra(graph, s - 1, f - 1))
