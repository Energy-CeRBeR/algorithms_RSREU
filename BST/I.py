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

    def height(self, node: Node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def print_leaves(self, node: Node):
        if node is None:
            return

        self.print_leaves(node.left)
        if node.left is None and node.right is None:
            print(node.data)

        self.print_leaves(node.right)

    def is_balanced(self, node: Node):
        if node is None:
            return True

        lh = self.height(node.left)
        rh = self.height(node.right)

        if (abs(lh - rh) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right)):
            return True

        return False


a = list(map(int, input().split()))
a.pop()

visited = set()
tree = BinaryTree()
for item in a:
    if item not in visited:
        tree.root = tree.insert(tree.root, item)
        visited.add(item)

print("YES" if tree.is_balanced(tree.root) else "NO")
