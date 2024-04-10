#include <bits/stdc++.h>

using namespace std;

class Tree
{
    struct Node
    {
        Node * left = nullptr;
        Node * right = nullptr;

        long long size = 1;
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

    std::vector<long long> values() const
    {
        std::vector<long long> result;
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

    static Node * merge(Node * first, Node * second)
    {
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
        
        if (getSize(node->left) >= z) {
            split(z, node->left, first, node->left);
            second = node;
        } else {
            split(z - getSize(node->left) - 1, node->right, node->right, second);
            first = node;
        }
        recalc(node);
    }

    static void clear(Node * node) {
        if (node) {
            clear(node->left);
            clear(node->right);
            delete node;
        }
    }

    static void values(std::vector<long long> & result, Node * node) {
        if (!node) {
            return;
        }
        values(result, node->left);
        result.push_back(node->x);
        values(result, node->right);
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
        tree.toStart(l - 1, r);

    }
    vector<long long> result = tree.values();
    for (size_t i = 0; i + 1 < result.size(); ++i) {
        cout << result[i] << ' ';
    }
    cout << result.back() << '\n';
}
