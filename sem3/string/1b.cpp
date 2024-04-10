#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    string p, t;
    cin >> p >> t;
    string s = p + "#" + t;
    vector<int> z(s.length(), 0);
    int left = 0, right = 0;
    for (int i = 1; i < s.length(); ++i) {
        z[i] = max(0, min(right - i, z[i - left]));
        while (i + z[i] < s.length() && s[z[i]] == s[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] > right) {
            left = i;
            right = i + z[i];
        }
    }
    vector<int> r;
    for (int i = p.length(); i < s.length(); ++i) {
        if (z[i] == p.length()) {
            r.push_back(i - p.length());
        }
    }
    cout << r.size() << '\n';
    for (const auto & i : r) {
        cout << i << ' ';
    }
}
