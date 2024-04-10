#include <iostream>
#include <vector>

class AVLTree
{
public:
    bool contains(long long value) const { return search(value, root); }
    bool insert(long long value) {
        bool result = insert(value, root);
        // if (result) {
        //     treeSize++;
        // }
        return result;
    }
    bool remove(long long value) {
        bool result = remove(value, root);
        // if (result) {
        //     treeSize--;
        // }
        return result;
    }

    std::size_t size() const { return getSize(root); }
    // std::size_t size() const { return treeSize; }
    bool empty() const { return size() == 0; }

    std::vector<long long> values() const {
        std::vector<long long> result;
        result.reserve(size());
        values(result, root);
        return result;
    }

    long long max(int k = 0) const {
        Node * node = root;
        while (k >= 0) {
            if (getSize(node->right) > k) {
                node = node->right;
            } else {
                k -= getSize(node->right) + 1;
                if (k >= 0) {
                    node = node->left;
                }
            }
        }
        return node->value;
    }

    ~AVLTree() { clear(root); }

private:
    struct Node
    {
        Node * left = nullptr;
        Node * right = nullptr;
        std::size_t height = 1;
        // 
        std::size_t size = 0;
        // 
        long long value;

        Node() = default;
        Node(long long value)
            : value(value)
        {
        }
    };

    using NodePtr = AVLTree::Node *;

    Node * root = nullptr;
    // std::size_t treeSize = 0;

    static bool search(long long value, Node * node) {
        if (!node) {
            return false;
        }
        if (value < node->value) {
            return search(value, node->left);
        }
        if (value > node->value) {
            return search(value, node->right);
        }
        return true;
    }

    //
    static std::size_t getSize(Node * node) {
        return (!node) ? 0 : node->size;
    }
    //

    static std::size_t getHeight(Node * node) {
        return (!node) ? 0 : node->height;
    }

    // static void recalcHeight(Node * node) {
    static void recalc(Node * node) {
        node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
        //
        node->size = 1 + getSize(node->left) + getSize(node->right);
        //
    }

    static Node * rotateLeft(Node * node) {
        Node * rightChild = node->right;
        node->right = rightChild->left;
        rightChild->left = node;
        recalc(node);
        recalc(rightChild);
        return rightChild;
    }

    static Node * rotateRight(Node * node) {
        Node * leftChild = node->left;
        node->left = leftChild->right;
        leftChild->right = node;
        recalc(node);
        recalc(leftChild);
        return leftChild;
    }
    static Node * balance(Node * node) {
        if (!node) {
            return nullptr;
        }
        recalc(node);
        long long difference = getHeight(node->left) - getHeight(node->right);
        if (difference == 2) {
            if (getHeight(node->left->right) > getHeight(node->left->left)) {
                node->left = rotateLeft(node->left);
            }
            return rotateRight(node);
        }
        else if (difference == -2) {
            if (getHeight(node->right->left) > getHeight(node->right->right)) {
                node->right = rotateRight(node->right);
            }
            return rotateLeft(node);
        }
        return node;
    }

    static bool insert(long long value, NodePtr & node) {
        bool result = (node == nullptr);
        if (result) {
            delete node;
            node = new Node(value);
        }
        else if (value < node->value) {
            result = insert(value, node->left);
        }
        else if (value > node->value) {
            result = insert(value, node->right);
        }
        node = balance(node);
        return result;
    }

    static long long findMin(Node * node) {
        while (node->left) {
            node = node->left;
        }
        return node->value;
    }

    static bool remove(long long value, NodePtr & node) {
        if (!node) {
            return false;
        }

        bool result = (value == node->value);
        if (result) {
            if (!node->right) {
                Node * leftChild = node->left;
                delete node;
                node = leftChild;
                // recalc(node);
                return true;
            }
            node->value = findMin(node->right);
            remove(node->value, node->right);
        }
        else if (value < node->value) {
            result = remove(value, node->left);
        }
        else if (value > node->value) {
            result = remove(value, node->right);
        }
        node = balance(node);
        return result;
    }

    static void values(std::vector<long long> & result, Node * node) {
        if (!node) {
            return;
        }

        values(result, node->left);
        result.push_back(node->value);
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
    long long n;
    std::cin >> n;

    AVLTree tree;

    for (long long i = 0; i < n; ++i) {
        long long c, k;
        std::cin >> c >> k;
        if (c == 1) {
            tree.insert(k);
        } else if (c == 0) {
            std::cout << tree.max(k - 1) << '\n';
        } else {
            tree.remove(k);
        }
    }
}