n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

hash_b = {i: 0 for i in set(sorted(b))}
for item in a:
    if item in hash_b:
        hash_b[item] += 1

result = list(hash_b[item] for item in b)
print(*result)
