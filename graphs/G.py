import sys

sys.setrecursionlimit(10000000)


def cycle_dfs(vertex, parent):
    global cycle
    color[vertex] = "Gray"
    for v in graph[vertex]:
        if v == parent:
            continue

        if color[v] == "White":
            cycle_dfs(v, vertex)

        if color[v] == "Gray":
            cycle = True

    color[vertex] = "Black"


def basic_dfs(start):
    global visited

    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            basic_dfs(v)


def check_cycle():
    global color
    global find

    color = ["White"] * (n + 1)
    cycle = False
    for i in range(1, n + 1):
        if color[i] == "White":
            cycle_dfs(i, 0)
            if cycle:
                break

    return cycle


def check_dist():
    global visited

    root = 1
    visited = [False] * (n + 1)
    basic_dfs(root)

    return all(x for x in visited[1:])


def is_tree():
    if n != m + 1:
        return False

    if check_cycle():
        return False

    if not check_dist():
        return False

    return True


n, m = map(int, input().split())

graph = {i: set() for i in range(n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


print("YES" if is_tree() else "NO")
