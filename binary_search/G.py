n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
left = 0
right = 10000001

while left < right - 1:
    middle = (left + right) // 2
    if sum(x // middle for x in a) < k:
        right = middle
    else:
        left = middle

print(left)
