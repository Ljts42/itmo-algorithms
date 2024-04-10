#include <bits/stdc++.h>

using namespace std;

class Tree
{
    struct Node
    {
        Node * left = nullptr;
        Node * right = nullptr;

        long long size = 1;
        bool rev = false;

        long long x;
        long long y;


        Node() = default;
        Node(long long value)
            : x(value)
            , y(rand())
        {
        }
    };

public:
    Tree() = default;
    Tree(long long value)
        : root(new Node(value))
    {
    }

    long long size() const { return getSize(root); }

    void insert(long long value)
    {
        if (!root) {
            root = new Node(value);
        } else {
            root = merge(root, new Node(value));
        }
    }

    vector<long long> values() const
    {
        vector<long long> result;
        result.reserve(size());
        values(result, root);
        return result;
    }

    void toStart(long long l, long long r)
    {
        Node * first = nullptr;
        Node * second = nullptr;
        Node * third = nullptr;

        split(l, root, first, second);
        split(r - l, second, second, third);

        root = merge(second, merge(first, third));
    }

    void reverse(long long l, long long r)
    {
        Node * first = nullptr;
        Node * second = nullptr;
        Node * third = nullptr;

        split(l, root, first, second);
        split(r - l, second, second, third);

        second->rev ^= true;
        root = merge(merge(first, second), third);
    }

    ~Tree() { clear(root); }

private:
    Node * root = nullptr;

    using NodePtr = Tree::Node *;

    static long long getSize(Node * node) {
        return (!node) ? 0 : node->size;
    }

    static void recalc(Node * node) {
        node->size = 1 + getSize(node->left) + getSize(node->right);
    }

    static void push(Node * node)
    {
        if (node != nullptr && node->rev) {
            node->rev = false;
            swap(node->left, node->right);
            if (node->left != nullptr) {
                node->left->rev ^= true;
            }
            if (node->right != nullptr) {
                node->right->rev ^= true;
            }
        }
    }

    static Node * merge(Node * first, Node * second)
    {
        push(first);
        push(second);
        if (!second) {
            return first;
        }
        if (!first) {
            return second;
        }
        if (first->y > second->y) {
            first->right = merge(first->right, second);
            recalc(first);
            return first;
        } else {
            second->left = merge(first, second->left);
            recalc(second);
            return second;
        }
    }

    static void split(long long z, Node * node, NodePtr & first, NodePtr & second)
    {
        if (!node) {
            first = nullptr;
            second = nullptr;
            return;
        }
        push(node);

        if (getSize(node->left) >= z) {
            split(z, node->left, first, node->left);
            second = node;
        } else {
            split(z - getSize(node->left) - 1, node->right, node->right, second);
            first = node;
        }
        recalc(node);
    }

    static void values(vector<long long> & result, Node * node) {
        if (!node) {
            return;
        }
        push(node);
        values(result, node->left);
        result.push_back(node->x);
        values(result, node->right);
    }

    static void clear(Node * node) {
        if (node) {
            clear(node->left);
            clear(node->right);
            delete node;
        }
    }
};

int main()
{
    long long n, m;
    cin >> n >> m;

    Tree tree;
    for (long long i = 1; i <= n; ++i) {
        tree.insert(i);
    }

    for (long long i = 0; i < m; ++i) {
        long long l, r;
        cin >> l >> r;
        tree.reverse(l - 1, r);

    }
    vector<long long> result = tree.values();
    for (size_t i = 0; i + 1 < result.size(); ++i) {
        cout << result[i] << ' ';
    }
    cout << result.back() << '\n';
}
