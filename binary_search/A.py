def binary_search(lst, n, target):
    left = 0
    right = n - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return True

        if lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for item in b:
    print("YES" if binary_search(a, n, item) else "NO")
