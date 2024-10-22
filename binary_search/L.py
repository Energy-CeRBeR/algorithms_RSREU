def hook(coeff):
    h = 0
    u = 0
    for i in range(len(diff)):
        u -= 1
        if u < 1 and diff[i] <= coeff:
            h += 1
            u = c
    if h >= r:
        return True
    return False


n, r, c = map(int, input().split())
heights = sorted([int(input()) for _ in range(n)])
diff = [heights[i + c - 1] - heights[i] for i in range(len(heights) - c + 1)]

left = -1
right = heights[-1] - heights[0]
if r > 1:
    while left + 1 < right:
        middle = (left + right) // 2
        if hook(middle):
            right = middle
        else:
            left = middle
    print(right)

else:
    print(min(diff))
