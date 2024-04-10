#include <bits/stdc++.h>

using namespace std;

constexpr int MAXN = 1e6;
set<int> g[MAXN];
int d[MAXN];
int r[MAXN];

void dfs(int i, int u) {
    for (auto j : g[i]) {
        if (d[i] + 1 < d[j]) {
            d[j] = d[i] + 1;
            r[j] = u;
            dfs(j, u);
        } else if (d[i] + 1 == d[j] && u < r[j]) {
            r[j] = u;
            dfs(j, u);
        }
    }
}

int main() {
    for (int i = 0; i < MAXN; ++i) {
        d[i] = MAXN;
        r[i] = MAXN;
    }

    int n, k, m;
    cin >> n >> k;
    int e[k];
    for (int i = 0; i < k; ++i) {
        cin >> e[i];
    }
    cin >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }
    
    for (auto u : e) {
        d[u] = 0;
        r[u] = u;
        dfs(u, u);
    }

    for (int i = 1; i < n; ++i) {
        cout << d[i] << ' ';
    }
    cout << d[n] << '\n';
    for (int i = 1; i <= n; ++i) {
        cout << r[i] << ' ';
    }
}
