from sys import stdin


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if int(arr[j + 1] + arr[j]) > int(arr[j] + arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


numbers = []
for line in stdin:
    numbers.append(line.strip())

print(int("".join(bubble_sort(numbers))))
