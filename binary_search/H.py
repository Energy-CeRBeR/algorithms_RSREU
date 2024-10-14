def check_answer(w, h, n, a):
    return (a // w) * (a // h) >= n


w, h, n = map(int, input().split())

left = 0
right = 10 ** 18
while left <= right:
    middle = (left + right) // 2
    if check_answer(w, h, n, middle):
        right = middle - 1
    else:
        left = middle + 1

print(left)
