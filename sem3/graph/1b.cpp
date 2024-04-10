#include <bits/stdc++.h>
 
using namespace std;

vector<map<long long, long long>> g;
vector<long long> p;
vector<bool> v;

void dfs(long long i) {
    v[i] = true;
    for (auto j : g[i]) {
        if (!v[j.first]) {
            dfs(j.first);
        }
    }
    p.push_back(i);
}

int main() {
    long long n, m, s, t;
    cin >> n >> m >> s >> t;
    --s; --t;
    g.resize(n);
    
    for (long long i = 0; i < m; ++i) {
        long long a, b, c;
        cin >> a >> b >> c;
        if (g[a - 1].count(b - 1) == 0) {
            g[a - 1][b - 1] = c;
        } else {
            g[a - 1][b - 1] = min(g[a - 1][b - 1], c);
        }
    }

    v.assign(n, false);
    dfs(s);

    vector<long long> r(n, 1e18);
    r[s] = 0;
    for (long long i = p.size() - 1; i >= 0; --i) {
        if (r[p[i]] == 1e18) {
            continue;
        }
        for (auto j : g[p[i]]) {
            r[j.first] = min(r[j.first], r[p[i]] + j.second);
        }
    }


    if (r[t] == 1e18) {
        cout << "Unreachable";
    } else {
        cout << r[t];
    }
}
