n = int(input())
a = sorted(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

hash_b = {i: 0 for i in set(sorted(b))}

i = 0
for key in hash_b:
    while i < n and a[i] < key:
        i += 1

    count = 0
    while i < n and a[i] == key:
        i += 1
        count += 1

    hash_b[key] = count


result = list(hash_b[item] for item in b)
print(*result)

print(hash_b)

