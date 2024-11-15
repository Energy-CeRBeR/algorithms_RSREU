n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))


def check_not_oriented():
    for i in range(n):
        if data[i][i] == 1:
            return False
        
        for j in range(n):
            if data[i][j] != data[j][i]:
                return False

    return True


print("YES" if check_not_oriented() else "NO")
