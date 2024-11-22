import heapq

INF = 10 ** 10


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


n = int(input())
gas_costs = list(map(int, input().split()))
m = int(input())

graph = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add((b, gas_costs[a - 1]))
    graph[b].add((a, gas_costs[b - 1]))

print(dijkstra(graph, 1, n))
