#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int data;
    int count;
    Node *left;
    Node *right;

    Node(int data) : data(data), count(1), left(nullptr), right(nullptr) {}
};

class BinaryTree
{
public:
    Node *root;

    BinaryTree() : root(nullptr) {}

    Node *insert(Node *node, int x)
    {
        if (node == nullptr)
        {
            return new Node(x);
        }

        if (x < node->data)
        {
            node->left = insert(node->left, x);
        }
        else
        {
            node->right = insert(node->right, x);
        }

        return node;
    }

    Node *search(Node *node, int x)
    {
        if (node == nullptr)
        {
            return nullptr;
        }

        if (x < node->data)
        {
            return search(node->left, x);
        }
        else if (x > node->data)
        {
            return search(node->right, x);
        }
        else
        {
            node->count++;
            return node;
        }
    }

    int get_max(Node *node)
    {
        Node *cur_node = node;
        while (cur_node->right != nullptr)
        {
            cur_node = cur_node->right;
        }
        return cur_node->data;
    }

    void print_sorted_tree(Node *node)
    {
        if (node == nullptr)
        {
            return;
        }

        print_sorted_tree(node->left);
        cout << node->data << " " << node->count << endl;
        print_sorted_tree(node->right);
    }
};

int main()
{
    vector<int> a;
    int input;
    cin >> input;
    while (input != 0)
    {
        a.push_back(input);
        cin >> input;
    }

    BinaryTree tree;
    for (int item : a)
    {
        if (tree.search(tree.root, item) == nullptr)
        {
            tree.root = tree.insert(tree.root, item);
        }
    }

    tree.print_sorted_tree(tree.root);

    return 0;
}