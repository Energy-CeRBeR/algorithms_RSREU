import sys


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

    def max_node(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current

    def remove(self, node: Node, x):
        if node is None:
            return None

        if x < node.data:
            node.left = self.remove(node.left, x)
        elif x > node.data:
            node.right = self.remove(node.right, x)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            max_node = self.max_node(node.left)
            node.data = max_node.data
            node.left = self.delete(node.left, max_node.data)

        return node

    def size(self, node: Node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

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
        print("." * level + str(node.data))
        self.print_tree(node.right, level + 1)


tree = BinaryTree()

query = sys.stdin.readline().split()
while query:
    if query[0] == "ADD":
        if not tree.search(tree.root, int(query[1])):
            tree.root = tree.insert(tree.root, int(query[1]))
            print("DONE")
        else:
            print("ALREADY")

    elif query[0] == "DELETE":
        if tree.search(tree.root, int(query[1])):
            tree.root = tree.remove(tree.root, int(query[1]))
            print("DONE")
        else:
            print("CANNOT")

    elif query[0] == "SEARCH":
        print("YES" if tree.search(tree.root, int(query[1])) else "NO")

    elif query[0] == "PRINTTREE":
        tree.print_tree(tree.root, 0)

    query = sys.stdin.readline().split()
