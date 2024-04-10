#include <bits/stdc++.h>

using namespace std;

struct node {
    node * left = nullptr;
    node * right = nullptr;
    bool terminal = false;
};

int main() {
    int n;
    cin >> n;
    node * r = new node();
    for (int i = 0; i < n; ++i) {
        string v;
        cin >> v;
        node * c = root;
        for (int j = 0; j < v.length(); ++j) {
            if (v[j] == '0') {
                if (c->left == nullptr) {
                    c->left = new node();
                }
                c = c->left;
            } else {
                if (c->right == nullptr) {
                    c->right = new node();
                }
                c = c->right;
            }
        }
        ///////////////////
    }
}
