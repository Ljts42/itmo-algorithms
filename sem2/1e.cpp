#include <bits/stdc++.h>

using namespace std;

long long MN = LLONG_MIN;
long long MX = LLONG_MAX;
// long long MN;
// long long MX;
long long n;
vector<long long> minv;
vector<long long> d;

void push(long long v) {
    if (d[v] == MN) {
        return;
    }

    if (minv[v] == MX) {
        minv[v] = d[v];
    } else {
        minv[v] = max(d[v], minv[v]);
    }

    if (v < n) {
        d[2 * v] = max(d[v], d[2 * v]);
        d[2 * v + 1] = max(d[v], d[2 * v + 1]);
    }

    d[v] = MN;
}

void update(long long l, long long r, long long q, long long v, long long vl, long long vr) {
    push(v);
    if (r <= vl || vr <= l) {
        return;
    }
    if (l <= vl && vr <= r) {
        d[v] = q;
        push(v);
        return;
    }

    long long vm = (vl + vr) / 2;
    update(l, r, q, 2 * v, vl, vm);
    update(l, r, q, 2 * v + 1, vm, vr);

    minv[v] = min(minv[2 * v], minv[2 * v + 1]);
}


long long query(long long l, long long r, long long v, long long vl, long long vr) {
    push(v);
    if (r <= vl || vr <= l) {
        return MX;
    }
    if (l <= vl && vr <= r) {
        return minv[v];
    }

    long long vm = (vl + vr) / 2;
    return min(query(l, r, 2 * v, vl, vm), query(l, r, 2 * v + 1, vm, vr));
}

int main() {
    freopen("rmq.in", "r", stdin);
    freopen("rmq.out", "w", stdout);

    long long N, m;
    cin >> N >> m;
    n = log(N - 1) / log(2) + 1;
    n = 1 << n;


    vector<vector<long long>> inp(m);
    inp[0].resize(3);
    cin >> inp[0][0] >> inp[0][1] >> inp[0][2];
    inp[0][0] -= 1;
    // MN = inp[0][2] - 1;
    // MX = inp[0][2] + 1;

    for (long long i = 1; i < m; ++i) {
        inp[i].resize(3);
        cin >> inp[i][0] >> inp[i][1] >> inp[i][2];
        inp[i][0] -= 1;

        // MN = min(MN, inp[i][2] - 1);
        // MX = max(MX, inp[i][2] + 1);
    }

    minv.resize(2 * n, MX);
    d.resize(2 * n, MN);

    for (long long i = 0; i < m; ++i) {
        update(inp[i][0], inp[i][1], inp[i][2], 1, 0, n);
    }

    for (long long i = 0; i < m; ++i) {
        if (query(inp[i][0], inp[i][1], 1, 0, n) != inp[i][2]) {
            cout << "inconsistent\n";
            return 0;
        }
    }

    cout << "consistent\n";
    for (long long i = 0; i < N; ++i) {
        long long k = query(i, i + 1, 1, 0, n);
        if (k == MX || k == MN) {
            cout << INT_MAX << ' ';
        } else {
            cout << k << ' ';
        }
    }
    return 0;
}