def f(x):
    return x ** 2 + x ** 0.5


def find_rood(c, eps):
    left = 0
    right = c ** 0.5
    while left < right:
        middle = (left + right) / 2

        f_x = f(middle)

        if abs(f_x - c) < eps:
            return middle

        if f_x < c:
            left = middle
        else:
            right = middle


c = float(input())
print(find_rood(c, 10e-7))
