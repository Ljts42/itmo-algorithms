#include <bits/stdc++.h>

using namespace std;

long long n;

long long genA(long long a) {
    return (23 * a + 21563) % 16714589;
}

long long genU(long long i, long long u, long long r) {
    return ((17 * u + 751 + r + 2 * i) % n) + 1;
}

long long genV(long long i, long long v, long long r) {
    return ((13 * v + 593 + r + 5 * i) % n) + 1;
}

int main() {
    long long m, u, v, r, k;
    cin >> n >> m;
    k = log(n) / log(2) + 1;
    long long st[n][k];
    cin >> st[0][0];

    for (long long i = 1; i < n; ++i) {
        st[i][0] = genA(st[i - 1][0]);
    }

    for (long long j = 1; j < k; ++j) {
        for (long long i = 0; i < n; ++i) {
            st[i][j] = st[i][j - 1];
            if (1 << (j - 1) < n - i) {
                st[i][j] = min(st[i][j], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    cin >> u >> v;

    for (long long i = 1; i <= m; ++i) {
        long long x = min(u, v);
        long long y = max(u, v);

        long long j = log(y - x + 1) / log(2);
        r = min(st[x - 1][j], st[y - (1 << j)][j]);

        if (i < m) {
            u = genU(i, u, r);
            v = genV(i, v, r);
        }
    }

    cout << u << ' ' << v << ' ' << r;
}