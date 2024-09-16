from collections import defaultdict


def is_anagram(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return False

    d1 = defaultdict(int)
    for c in s1:
        d1[c] += 1

    d2 = defaultdict(int)
    for c in s2:
        d2[c] += 1

    for key in d1:
        if d1[key] != d2[key]:
            return False
    return True


a = input()
b = input()
print("YES" if is_anagram(a, b) else "NO")
