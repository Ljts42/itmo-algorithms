#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int n;
    vector<pair<int, int>> c;
    cin >> n;
    vector<vector<pair<float, int>>> g(n);
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        for (int j = 0; j < c.size(); ++j) {
            float w = -hypot(x - c[j].first, y - c[j].second);
            g[j].push_back({w, c.size()});
            g[c.size()].push_back({w, j});
        }
        c.push_back({x, y});
    }
    vector<bool> v(n, false);
    v[0] = true;
    priority_queue<pair<float, int>> q;
    float r = 0;
    for (auto & i : g[0]) {
        q.push(i);
    }
    int k = 1;
    while (k < n) {
        pair<float, int> t;
        while (!q.empty()) {
            t = q.top();
            q.pop();
            if (!v[t.second]) {
                r -= t.first;
                break;
            }
        }
        v[t.second] = true;
        for (auto & i : g[t.second]) {
            if (!v[i.second]) {
                q.push(i);
            }
        }
        ++k;
    }
    cout.precision(10);
    cout << r;
}
