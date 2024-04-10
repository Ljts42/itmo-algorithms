#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    for (int i = n / 2; i >= 0; --i) {
        bool f = true;
        for (int j = 0; j < i; ++j) {
            if (s[i + j] != s[i - j - 1]) {
                f = false;
                break;
            }
        }
        if (f) {
            cout << n - i << ' ';
        }
    }
}
