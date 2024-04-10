#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n;
    cin >> n;
    long long k = (log(n) / log(2)) + 1;

    vector<vector<long long>> p;
    p.resize(n);
    vector<long long> d(n, 0);
    p[0].resize(k);
    for (long long i = 1; i < n; ++i) {
        p[i].resize(k);
        cin >> p[i][0];
        --p[i][0];
        d[i] = d[p[i][0]] + 1;
    }

    for (long long j = 1; j < k; ++j) {
        for (long long i = 1; i < n; ++i) {
            p[i][j] = p[p[i][j - 1]][j - 1];
        }
    }
    long long m;
    cin >> m;
    for (long long j = 0; j < m; ++j) {
        long long u, v;
        cin >> u >> v;
        --u;
        --v;
        if (d[u] > d[v]) {
            swap(u, v);
        }
        for (long long i = k - 1; i >= 0; --i) {
            if (d[p[v][i]] >= d[u]) {
                v = p[v][i];
            }
        }
        if (u != v) {
            for (long long i = k - 1; i >= 0; --i) {
                if (p[u][i] != p[v][i]) {
                    u = p[u][i];
                    v = p[v][i];
                }
            }
            cout << p[u][0] + 1L << '\n';
        } else {
            cout << u + 1L << '\n';
        }
    }
}
