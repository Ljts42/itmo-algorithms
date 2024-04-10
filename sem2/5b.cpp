#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int k = (log(n) / log(2)) + 1;

    vector<vector<pair<int, int>>> p;
    p.resize(n);
    p[0].resize(k);
    p[0][0] = make_pair(0, INT_MAX);

    vector<int> d(n, 0);

    for (int i = 1; i < n; ++i) {
        p[i].resize(k);

        int a, b;
        cin >> a >> b;
        p[i][0] = make_pair(a - 1, b);

        d[i] = d[p[i][0].first] + 1;
    }

    for (int j = 1; j < k; ++j) {
        p[0][j].first = p[0][j - 1].first;
        p[0][j].second = p[0][j - 1].second;
    }

    for (int j = 1; j < k; ++j) {
        for (int i = 1; i < n; ++i) {
            p[i][j].first = p[p[i][j - 1].first][j - 1].first;
            p[i][j].second = min(p[i][j - 1].second,
                                 p[p[i][j - 1].first][j - 1].second);
        }
    }
    int m;
    cin >> m;
    for (int inp = 0; inp < m; ++inp) {
        int u, v;
        cin >> u >> v;
        u -= 1;
        v -= 1;
        if (d[u] > d[v]) {
            swap(u, v);
        }
        int res = INT_MAX;
        for (int i = k - 1; i >= 0; --i) {
            if (d[p[v][i].first] >= d[u]) {
                res = min(res, p[v][i].second);
                v = p[v][i].first;
            }
        }
        if (u != v) {
            for (int i = k - 1; i >= 0; --i) {
                if (p[u][i].first != p[v][i].first) {
                    res = min(res, min(p[u][i].second, p[v][i].second));
                    u = p[u][i].first;
                    v = p[v][i].first;
                }
            }
            cout << min(res, min(p[u][0].second, p[v][0].second)) << '\n';
        } else {
            cout << res << '\n';
        }
    }
}
