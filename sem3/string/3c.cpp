#include <bits/stdc++.h>

using namespace std;

void count_sort(vector<int> & p, vector<int> & c) {
    int n = p.size();
    vector<int> cnt(n);
    for (auto & x : c) {
        cnt[x]++;
    }
    vector<int> p_new(n);
    vector<int> pos(n);
    pos[0] = 0;
    for (int i = 1; i < n; ++i) {
        pos[i] = pos[i - 1] + cnt[i - 1];
    }
    for (auto x : p) {
        int i = c[x];
        p_new[pos[i]] = x;
        ++pos[i];
    }
    p = p_new;
}


int main() {
    int m;
    cin >> m;
    vector<string> t(m);
    for (int i = 0; i < m; ++i) {
        cin >> t[i];
    }
    string s;
    cin >> s;
    s += "$";
    int n = s.size();

    vector<int> p(n), c(n);
    vector<pair<char, int>> a(n);
    for (int i = 0; i < n; ++i) {
        a[i] = {s[i], i};
    }
    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        p[i] = a[i].second;
    }
    c[p[0]] = 0;

    for (int i = 1; i < n; ++i) {
        if (a[i].first == a[i - 1].first) {
            c[p[i]] = c[p[i - 1]];
        } else {
            c[p[i]] = c[p[i - 1]] + 1;
        }
    }

    int k = 0;
    while ((1 << k) < n) {
        for (int i = 0; i < n; ++i) {
            p[i] = (p[i] - (1 << k) + n) % n;
        }
        count_sort(p, c);

        vector<int> c_new(n);
        c_new[p[0]] = 0;

        for (int i = 1; i < n; ++i) {
            pair<int, int> prev = {c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n]};
            pair<int, int> now = {c[p[i]], c[(p[i] + (1 << k)) % n]};
            if (now == prev) {
                c_new[p[i]] = c_new[p[i - 1]];
            } else {
                c_new[p[i]] = c_new[p[i - 1]] + 1;
            }
        }
        c = c_new;
        k++;
    }
    
    // for (int i = 0; i < n; ++i) {
    //     cout << p[i] << " " << s.substr(p[i], n - p[i]) << "\n";
    // }
    for (int i = 0; i < m; ++i) {
        auto left = p.begin();
        auto right = p.end();
        for (int j = 0; j < t[i].length(); ++j) {
            auto comp = [&s, j](int suf, char to_find) {
                return s[suf + j] < to_find;
            };
            left = lower_bound(left, right, t[i][j], comp);
            
            auto comp2 = [&s, j](char to_find, int suf) {
                return to_find < s[suf + j];
            };
            right = upper_bound(left, right, t[i][j], comp2);
        }
        cout << static_cast<int>(right - left) << '\n';
    }
}
