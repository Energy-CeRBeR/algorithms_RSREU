from collections import defaultdict


def check_full():
    for lst_v in graph.values():
        if len(lst_v) != n - 1:
            return False
    return True


n, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print("YES" if check_full() else "NO")
