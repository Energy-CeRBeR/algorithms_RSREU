class Node:
    def __init__(self, data):
        self.data = data
        self.count = 1
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

    def search(self, node: Node, x):
        if node is None:
            return False

        if x < node.data:
            return self.search(node.left, x)
        elif x > node.data:
            return self.search(node.right, x)
        else:
            node.count += 1

        return node

    def get_max(self, node: Node):
        cur_node = node
        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node.data

    def print_sorted_tree(self, node: Node):
        if node is None:
            return

        self.print_sorted_tree(node.left)
        print(node.data, node.count)
        self.print_sorted_tree(node.right)


a = list(map(int, input().split()))
a.pop()

tree = BinaryTree()
for item in a:
    if tree.search(tree.root, item) == False:
        tree.root = tree.insert(tree.root, item)

tree.print_sorted_tree(tree.root)
