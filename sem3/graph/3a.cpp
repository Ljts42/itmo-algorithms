#include <bits/stdc++.h>

using namespace std;

vector<set<int>> g;
vector<set<int>> b;
vector<int> e;
vector<int> r;
vector<int> v;
vector<int> c;

void dfs(int i, int p = -1) {
    v[i] = true;
    e[i] = (p == -1) ? 0 : e[p] + 1;
    r[i] = (p == -1) ? 0 : e[p] + 1;
    for (auto j : g[i]) {
        if (j == p) continue;
        if (v[j]) {
            r[i] = min(r[i], e[j]);
        } else {
            dfs(j, i);
            r[i] = min(r[i], r[j]);
            if (r[j] > e[i]) {
                b[i].insert(j);
                b[j].insert(i);
            }
        }
    }
}

void dfs2(int i, int t) {
    c[i] = t;
    for (auto j : b[i]) {
        if (c[j] == -1) {
            dfs2(j, t);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    g.resize(n);
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        g[x - 1].insert(y - 1);
        g[y - 1].insert(x - 1);
    }
    
    e.resize(n);
    r.resize(n);
    v.resize(n);
    b.resize(n);
    c.resize(n);
    for (int i = 0; i < n; ++i) {
        e[i] = 999999;
        r[i] = 999999;
        v[i] = false;
        c[i] = -1;
    }

    for (int i = 0; i < n; ++i) {
        if (!v[i]) {
            dfs(i);
        }
    }
    
    int t = 0;
    for (int i = 0; i < n; ++i) {
        if (c[i] == -1) {
            dfs2(i, t);
            t += 1;
        }
    }

    vector<int> k(t, -1);
    for (int i = 0; i < n; ++i) {
        k[c[i]] += 1;
    }

    long long res = 0;
    for (int i = 0; i < n; ++i) {
        res += k[c[i]] - b[i].size();
    }
    res /= 2;

    cout << res;
}
