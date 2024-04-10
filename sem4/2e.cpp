#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    size_t n;
    cin >> n;

    vector<vector<size_t>> r(n + 1, vector<size_t>(n));
    vector<vector<size_t>> d(n, vector<size_t>(n + 1));
    vector<vector<size_t>> l(n + 1, vector<size_t>(n));
    vector<vector<size_t>> u(n, vector<size_t>(n + 1));

    for (size_t i = 0; i <= n; i++) {
        for (size_t j = 0; j < n; j++) {
            cin >> r[i][j];
        }
    }

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j <= n; j++) {
            cin >> d[i][j];
        }
    }

    for (size_t i = 0; i <= n; i++) {
        for (size_t j = 0; j < n; j++) {
            cin >> l[i][j];
        }
    }

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j <= n; j++) {
            cin >> u[i][j];
        }
    }

    unordered_map<size_t, unordered_map<size_t, size_t>> g;
    g[0] = unordered_map<size_t, size_t>();
    
    for (size_t i = 0; i < n; i++) {
        if (g[0].count(i * n + 1) == 0)
            g[0][i * n + 1] = 1e9;
        g[0][i * n + 1] = min(g[0][i * n + 1], d[i][0]);
        if (g[0].count(n * n - n + i + 1) == 0)
            g[0][n * n - n + i + 1] = 1e9;
        g[0][n * n - n + i + 1] = min(g[0][n * n - n + i + 1], r[n][i]);
        
        if (g.count(i + 1) == 0)
            g[i + 1] = unordered_map<size_t, size_t>();
        if (g[i + 1].count(n * n + 1) == 0)
            g[i + 1][n * n + 1] = 1e9;
        g[i + 1][n * n + 1] = min(g[i + 1][n * n + 1], r[0][i]);
        
        if (g.count(i * n + n) == 0)
            g[i * n + n] = unordered_map<size_t, size_t>();
        if (g[i * n + n].count(n * n + 1) == 0)
            g[i * n + n][n * n + 1] = 1e9;
        g[i * n + n][n * n + 1] = min(g[i * n + n][n * n + 1], d[i][n]);
    }
    
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            if (g.count(i * n + j + 1) == 0)
                g[i * n + j + 1] = unordered_map<size_t, size_t>();
            if (i != 0) {
                if (g[i * n + j + 1].count((i - 1) * n + j + 1) == 0)
                    g[i * n + j + 1][(i - 1) * n + j + 1] = 1e9;
                g[i * n + j + 1][(i - 1) * n + j + 1] = min(g[i * n + j + 1][(i - 1) * n + j + 1], r[i][j]);
            }
            if (i != n - 1) {
                if (g[i * n + j + 1].count((i + 1) * n + j + 1) == 0)
                    g[i * n + j + 1][(i + 1) * n + j + 1] = 1e9;
                g[i * n + j + 1][(i + 1) * n + j + 1] = min(g[i * n + j + 1][(i + 1) * n + j + 1], l[i + 1][j]);
            }
            if (j != 0) {
                if (g[i * n + j + 1].count(i * n + j) == 0)
                    g[i * n + j + 1][i * n + j] = 1e9;
                g[i * n + j + 1][i * n + j] = min(g[i * n + j + 1][i * n + j], u[i][j]);
            }
            if (j != n - 1) {
                if (g[i * n + j + 1].count(i * n + j + 2) == 0)
                    g[i * n + j + 1][i * n + j + 2] = 1e9;
                g[i * n + j + 1][i * n + j + 2] = min(g[i * n + j + 1][i * n + j + 2], d[i][j + 1]);
            }
        }
    }

    vector<size_t> m(n * n + 2, 1e9);
    m[0] = 0;
    vector<bool> v(n * n + 2, false);
    multiset<pair<size_t, size_t>> q;
    q.insert({0, 0});
    while (!q.empty()) {
        size_t k = q.begin()->second;
        q.erase(q.begin());

        if (v[k] || m[k] >= 1e9 || k == n * n + 1) {
            break;
        }

        v[k] = true;

        if (g.count(k) != 0) {
            for (auto it = g[k].begin(); it != g[k].end(); ++it) {
                if (m[k] + it->second < m[it->first]) {
                    if (!v[it->first]) {
                        auto p = q.find({m[it->first], it->first});
                        if (p != q.end()) {
                            q.erase(p);
                        }
                        q.insert({m[k] + it->second, it->first});
                    }
                    m[it->first] = m[k] + it->second;
                }
            }
        }
    }

    cout << m[m.size() - 1];

    return 0;
}