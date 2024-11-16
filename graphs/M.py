def check(graph, n):
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0

            while stack:
                v = stack.pop()
                for u in graph[v]:
                    if color[u] == -1:
                        stack.append(u)
                        color[u] = 1 - color[v]
                    elif color[u] == color[v]:
                        return False, []

    table_1 = [i + 1 for i in range(n) if color[i] == 0]
    return True, table_1


n, m = map(int, input().split())
graph = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


answer, table_1 = check(graph, n)
if answer:
    print("YES")
    print(*table_1)
else:
    print("NO")
