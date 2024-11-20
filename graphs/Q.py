from collections import defaultdict, deque


def bfs():
    while queue:
        current, distance = queue.popleft()

        if field[current[0]][current[1]] == 2:
            return distance

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return -1


n, m = map(int, input().split())

field = list(list(map(int, input().split()))for _ in range(n))

good_positions = set()
graph = defaultdict(set)

for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            cur_x = i
            cur_y = j
            flag = False
            while cur_x + 1 < n and field[cur_x + 1][cur_y] != 1:
                cur_x += 1
                if field[cur_x][cur_y] == 2:
                    graph[(i, j)].add((cur_x, cur_y))
                    flag = True
                    break

            if not flag and (i, j) != (cur_x, cur_y):
                graph[(i, j)].add((cur_x, cur_y))

            cur_x = i
            cur_y = j
            flag = False
            while cur_x - 1 >= 0 and field[cur_x - 1][cur_y] != 1:
                cur_x -= 1
                if field[cur_x][cur_y] == 2:
                    graph[(i, j)].add((cur_x, cur_y))
                    flag = True
                    break

            if not flag and (i, j) != (cur_x, cur_y):
                graph[(i, j)].add((cur_x, cur_y))

            cur_x = i
            cur_y = j
            flag = False
            while cur_y + 1 < m and field[cur_x][cur_y + 1] != 1:
                cur_y += 1
                if field[cur_x][cur_y] == 2:
                    graph[(i, j)].add((cur_x, cur_y))
                    flag = True
                    break

            if not flag and (i, j) != (cur_x, cur_y):
                graph[(i, j)].add((cur_x, cur_y))

            cur_x = i
            cur_y = j
            flag = False
            while cur_y - 1 >= 0 and field[cur_x][cur_y - 1] != 1:
                cur_y -= 1
                if field[cur_x][cur_y] == 2:
                    graph[(i, j)].add((cur_x, cur_y))
                    flag = True
                    break

            if not flag and (i, j) != (cur_x, cur_y):
                graph[(i, j)].add((cur_x, cur_y))


start = (0, 0)
queue = deque([(start, 0)])
visited = set()
visited.add(start)

result = bfs()
print(result)
