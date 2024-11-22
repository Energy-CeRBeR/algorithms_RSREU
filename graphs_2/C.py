import heapq


def dijkstra(graph, start, end):
    pq = []

    dist = {node: INF for node in graph}
    prev = {node: -1 for node in graph}
    dist[start] = 0

    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_vertex == end:
            return dist[end], prev

        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex]:
            d = cur_dist + weight
            if d < dist[neighbor]:
                dist[neighbor] = d
                prev[neighbor] = cur_vertex
                heapq.heappush(pq, (d, neighbor))

    return INF, []


INF = 10 ** 10

n, s, f = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

graph = {i: set() for i in range(1, n + 1)}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i - 1][j - 1] != -1 and i != j:
            graph[i].add((j, a[i - 1][j - 1]))

result = dijkstra(graph, s, f)

if result[0] == INF:
    print(-1)

else:
    min_path, prev = result
    cur_vertex = f
    ans = [cur_vertex]
    while prev[cur_vertex] != -1:
        cur_vertex = prev[cur_vertex]
        ans.append(cur_vertex)
    print(*ans[::-1])
