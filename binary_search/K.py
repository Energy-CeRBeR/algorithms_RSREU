def get_max_count(worker, mx_time):
    days = 0
    while (mx_time >= worker[0]):
        mx_time -= worker[0]
        days += 1
        if days % worker[1] == 0:
            mx_time -= worker[2]

    return days


def check_answer(mx_time):
    return sum(get_max_count(worker, mx_time) for worker in data) >= m


m, n = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))

left = 0
right = 2 * 10 ** 5
while left < right:
    middle = (left + right) // 2
    cur_res = check_answer(middle)
    if check_answer(middle):
        right = middle
    else:
        left = middle + 1

print(right)
for worker in data:
    time = min(m, get_max_count(worker, right))
    print(time, end=" ")
    m -= time
