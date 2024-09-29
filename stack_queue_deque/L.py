a = [-1] + list(map(int, input().split()))[1:]
n = len(a)

stack = [(0, -1)]
mx = 0
k = 1
while k < n:
    h = a[k]

    if h >= stack[-1][1]:
        stack.append((k, h))

    else:
        ind = k
        while h < stack[-1][-1]:
            data = stack.pop()
            ind = data[0]
            mx = max(mx, (k - ind) * data[1])
        stack.append((ind, h))

    k += 1

while stack:
    data = stack.pop()
    mx = max(mx, (n - data[0]) * data[1])

print(mx)
