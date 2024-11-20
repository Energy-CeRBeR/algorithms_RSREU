from collections import deque


def get_next_moves(pos):
    x, y = pos
    moves = [
        (x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2),
        (x + 1, y - 2), (x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1)
    ]
    next_moves = []
    for next_x, next_y in moves:
        if 0 <= next_x < 8 and 0 <= next_y < 8:
            next_moves.append((next_x, next_y))
    return next_moves


def bfs():
    while queue:
        red_pos, green_pos, dist = queue.popleft()
        if red_pos == green_pos:
            return dist

        for next_red_pos in get_next_moves(red_pos):
            for next_green_pos in get_next_moves(green_pos):
                next_state = (next_red_pos, next_green_pos)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_red_pos, next_green_pos, dist + 1))

    return -1


start_red, start_green = input().split()
start_red = (ord(start_red[0]) - ord('a'), int(start_red[1]) - 1)
start_green = (ord(start_green[0]) - ord('a'), int(start_green[1]) - 1)

queue = deque([(start_red, start_green, 0)])
visited = set()
visited.add((start_red, start_green))

result = bfs()
print(result)
