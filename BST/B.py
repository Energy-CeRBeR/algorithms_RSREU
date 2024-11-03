class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node: Node, x):
        if node is None:
            return Node(x)

        if x < node.data:
            node.left = self.insert(node.left, x)
        else:
            node.right = self.insert(node.right, x)

        return node

    def find_min_node(self, node: Node):
        while node.left:
            node = node.left
        return node

    def remove(self, node: Node, x):
        if node is None:
            return None

        if x < node.data:
            node.left = self.remove(node.left, x)
        elif x > node.data:
            node.right = self.remove(node.right, x)

        elif not (node.left is None or node.right is None):
            node.data = self.find_min_node(node.right).data
            node.right = self.remove(node.right, node.data)

        elif not (node.left is None):
            node = node.left

        elif not (node.right is None):
            node = node.right

        else:
            node = None

        return node

    def size(self, node: Node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node: Node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def search(self, node: Node, x):
        if node is None:
            return False

        if x < node.data:
            return self.search(node.left, x)
        elif x > node.data:
            return self.search(node.right, x)

        return True

    def print_tree(self, node: Node, level=0):
        if node is None:
            return

        self.print_tree(node.left, level + 1)
        for _ in range(level):
            print(".", end="")
        print(node.data)
        self.print_tree(node.right, level + 1)


a = list(map(int, input().split()))
a.pop()

visited = set()
tree = BinaryTree()
for item in a:
    if item not in visited:
        tree.root = tree.insert(tree.root, item)
        visited.add(item)

print(tree.height(tree.root))
