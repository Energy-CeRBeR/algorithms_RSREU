#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;

    Node(int data) : data(data), left(nullptr), right(nullptr) {}
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

    int height(Node *node)
    {
        if (node == nullptr)
            return 0;
        return 1 + max(this->height(node->left), this->height(node->right));
    }

    bool isBalanced(Node *node)
    {
        if (node == nullptr)
            return true;

        int lh = this->height(node->left);
        int rh = this->height(node->right);

        if (abs(lh - rh) <= 1 && this->isBalanced(node->left) && this->isBalanced(node->right))
            return true;

        return false;
    }

    void print_leaves(Node *node)
    {
        if (node == nullptr)
            return;

        print_leaves(node->left);
        if (node->left == nullptr && node->right != nullptr || node->left != nullptr && node->right == nullptr)
            cout << node->data << endl;

        print_leaves(node->right);
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

    set<int> visited;
    BinaryTree tree;
    for (int item : a)
    {
        if (visited.find(item) == visited.end())
        {
            tree.root = tree.insert(tree.root, item);
            visited.insert(item);
        }
    }

    cout << (tree.isBalanced(tree.root) ? "YES" : "NO");

    return 0;
}