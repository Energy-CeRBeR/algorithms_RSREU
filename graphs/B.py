from copy import deepcopy


n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))


dict_template = {
    "in": set(),
    "out": set()
}

graph = {i: deepcopy(dict_template) for i in range(n)}
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[i]["out"].add(j)
            graph[j]["in"].add(i)


in_lst = []
out_lst = []
for i in range(n):
    if not graph[i]["in"]:
        in_lst.append(i + 1)
    if not graph[i]["out"]:
        out_lst.append(i + 1)


print(len(in_lst))
print(*in_lst, sep="\n")

print(len(out_lst))
print(*out_lst, sep="\n")
