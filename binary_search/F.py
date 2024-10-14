def calculate(time, x, y, target):
    return (time // x + time // y) >= target


n, x, y = map(int, input().split())

n -= 1
cur_time = min(x, y)

left = 0
right = 10 ** 9
while left <= right:
    middle = (left + right) // 2

    if calculate(middle, x, y, n):
        right = middle - 1
    else:
        left = middle + 1

print(left + cur_time)