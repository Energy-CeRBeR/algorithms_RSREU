import heapq


def dijkstra(graph, start):

    dist = {node: INF for node in graph}
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex]:
            d = cur_dist + weight
            if d < dist[neighbor]:
                dist[neighbor] = d
                heapq.heappush(pq, (d, neighbor))

    return dist.values()


INF = 2009000999

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())

    graph = {i: set() for i in range(n)}
    for _ in range(m):
        a, b, weight = map(int, input().split())
        graph[a].add((b, weight))
        graph[b].add((a, weight))

    start = int(input())
    print(*dijkstra(graph, start))
