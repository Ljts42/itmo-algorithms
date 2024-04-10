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
    string s;
    cin >> s;
    s += "$";
    int n = s.size();

    vector<int> suf(n), c(n);
    vector<pair<char, int>> a(n);
    for (int i = 0; i < n; ++i) {
        a[i] = {s[i], i};
    }
    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        suf[i] = a[i].second;
    }
    c[suf[0]] = 0;

    for (int i = 1; i < n; ++i) {
        if (a[i].first == a[i - 1].first) {
            c[suf[i]] = c[suf[i - 1]];
        } else {
            c[suf[i]] = c[suf[i - 1]] + 1;
        }
    }

    int k = 0;
    while ((1 << k) < n) {
        for (int i = 0; i < n; ++i) {
            suf[i] = (suf[i] - (1 << k) + n) % n;
        }
        count_sort(suf, c);

        vector<int> c_new(n);
        c_new[suf[0]] = 0;

        for (int i = 1; i < n; ++i) {
            pair<int, int> prev = {c[suf[i - 1]], c[(suf[i - 1] + (1 << k)) % n]};
            pair<int, int> now = {c[suf[i]], c[(suf[i] + (1 << k)) % n]};
            if (now == prev) {
                c_new[suf[i]] = c_new[suf[i - 1]];
            } else {
                c_new[suf[i]] = c_new[suf[i - 1]] + 1;
            }
        }
        c = c_new;
        k++;
    }

    vector<int> lcp(n);
    vector<int> pos(n);
    for (int i = 0; i < n; ++i) {
        pos[suf[i]] = i;
    }
    k = 0;
    for (int i = 0; i < n; ++i) {
        if (k > 0) {
            --k;
        }
        if (pos[i] + 1 == n) {
            lcp[n - 1] = -1;
            k = 0;
            continue;
        } else {
            int j = suf[pos[i] + 1];
            while (max(i, j) + k < n && s[i + k] == s[j + k]) {
                ++k;
            }
            lcp[pos[i]] = k;
        }
    }

    long long r = 0;
    for (int i = 1; i < suf.size(); ++i) {
        r += n - suf[i] - 1;
    }
    for (int i = 1; i < lcp.size() - 1; ++i) {
        r -= lcp[i];
    }
    cout << r;
}
