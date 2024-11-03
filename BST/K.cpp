#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int value;
    Node *left;
    Node *right;

    Node(int value) : value(value), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
public:
    Node *root;

    BinarySearchTree() : root(nullptr) {}

    void insert(int value)
    {
        if (root == nullptr)
        {
            root = new Node(value);
        }
        else
        {
            _insert_recursive(root, value);
        }
    }

    void _insert_recursive(Node *node, int value)
    {
        if (value < node->value)
        {
            if (node->left == nullptr)
            {
                node->left = new Node(value);
            }
            else
            {
                _insert_recursive(node->left, value);
            }
        }
        else if (value > node->value)
        {
            if (node->right == nullptr)
            {
                node->right = new Node(value);
            }
            else
            {
                _insert_recursive(node->right, value);
            }
        }
    }

    int find_min_greater_equal(int value)
    {
        return _find_min_greater_equal_recursive(root, value);
    }

    int _find_min_greater_equal_recursive(Node *node, int value)
    {
        if (node == nullptr)
        {
            return -1;
        }
        if (node->value >= value)
        {
            int left_result = _find_min_greater_equal_recursive(node->left, value);
            if (left_result != -1)
            {
                return left_result;
            }
            return node->value;
        }
        return _find_min_greater_equal_recursive(node->right, value);
    }
};

int main()
{
    int n;
    cin >> n;

    int flag = -2;
    BinarySearchTree bst;

    for (int i = 0; i < n; ++i)
    {
        string query;
        cin >> query;

        if (query == "+")
        {
            int value;
            cin >> value;
            if (flag == -2)
            {
                bst.insert(value);
            }
            else
            {
                bst.insert((flag + value) % (1000000000));
            }
            flag = -2;
        }
        else if (query == "?")
        {
            int value;
            cin >> value;
            int result = bst.find_min_greater_equal(value);
            flag = result;
            cout << result << endl;
        }
    }

    return 0;
}