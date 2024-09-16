class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __find_distance(self):
        return self.x ** 2 + self.y ** 2

    def __lt__(self, other):
        return self.__find_distance() < other.__find_distance()

    def __le__(self, other):
        return self.__find_distance() <= other.__find_distance()

    def __eq__(self, other):
        return self.__find_distance() == other.__find_distance()

    def __str__(self):
        return f"{self.x} {self.y}"


n = int(input())

points = list()
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))
points.sort()

print(*points, sep="\n")
