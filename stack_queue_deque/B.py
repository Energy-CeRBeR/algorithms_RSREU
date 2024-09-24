def check_result(s):
    stack = list()

    converter = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if stack and converter[c] == stack[-1]:
                stack.pop()
            else:
                return "no"

    return "yes" if not stack else "no"


s = input()
print(check_result(s))
