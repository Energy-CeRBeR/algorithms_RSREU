s = input().split()


def calculate(a, sign, b):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b


stack = list()
for c in s:
    if c.isdigit():
        stack.append(int(c))
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, c, b))

print(stack.pop())
