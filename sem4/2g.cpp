#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <unordered_set>
#include <sstream>

using namespace std;

pair<unordered_map<int, unordered_map<int, int>>, int> inp() {
    int n;
    cin >> n;
    unordered_map<int, unordered_map<int, int>> c;

    string s, w;
    getline(cin, s);
    getline(cin, s);
    stringstream z(s);
    while (z >> w) {
        int h = hash<string> {}(w);
        c[h][-h] = 1;
        c[-h][h] = 0;
        c[0][h] = 1;
        c[h][0] = 0;
    }
    if (n == 1) {
        cout << 0 << '\n';
        return make_pair(c, n);
    }
    string s2, w2;
    getline(cin, s2);
    stringstream z2(s2);
    while (z2 >> w2) {
        int h = hash<string> {}(w2);
        c[h][-h] = 1;
        c[-h][h] = 0;
        c[-h][-1] = 1;
        c[-1][-h] = 0;
    }
    for (int j = 1; j < n - 1; ++j) {
        string s3, w3;
        getline(cin, s3);
        stringstream z3(s3);
        while (z3 >> w3) {
            int h = hash<string> {}(w3);
            c[h][-h] = 1;
            c[-h][h] = 0;
            c[-h][j] = 1;
            c[j][-h] = 0;
            c[j][h] = 1;
            c[h][j] = 0;
        }
    }
    return make_pair(c, n);
}

pair<unordered_map<int, unordered_map<int, int>>, bool> bfs(unordered_map<int, unordered_map<int, int>>& f, int h,
        unordered_map<int, unordered_map<int, int>>& c, int s, int t) {
    unordered_map<int, unordered_map<int, int> > g;
    unordered_set<int> cur;
    unordered_set<int> con;
    cur.insert(s);
    while (!cur.empty()) {
        int i = *cur.begin();
        cur.erase(cur.begin());
        if (c.count(i) == 0) continue;
        for (const auto& j : c[i]) {
            if (g.count(j.first) == 0) {
                int d = c[i][j.first];
                if (f.count(i) > 0 && f[i].count(j.first) > 0)
                    d -= f[i][j.first];
                d -= d % h;
                if (d > 0) {
                    if (g.count(i) == 0)
                        g[i] = unordered_map<int, int>();
                    g[i][j.first] = d;
                    con.insert(j.first);
                }
            }
        }
        if (cur.empty()) {
            if (con.count(t) > 0) {
                return make_pair(g, true);
            } else {
                swap(cur, con);
                con.clear();
            }
        }
    }
    return make_pair(g, false);
}

int dfs(unordered_map<int, unordered_map<int, int> >& f, unordered_map<int, unordered_map<int, int> >& g, int i, int m, int t) {
    if (i == t || m == 0) {
        return m;
    }
    if (g.find(i) == g.end()) {
        return 0;
    }
    int res = 0;
    for (auto it = g[i].begin(); it != g[i].end();) {
        int j = it->first;
        int d = dfs(f, g, j, min(m - res, g[i][j]), t);
        res += d;
        if (d == 0 || g[i][j] == d) {
            it = g[i].erase(it);
        } else {
            g[i][j] -= d;
            ++it;
        }
        if (d > 0) {
            f[i][j] += d;
            if (f.count(j) == 0)
                f[j] = unordered_map<int, int>();
            if (f[j].count(i) == 0)
                f[j][i] = 0;
            f[j][i] -= d;
        }
        if (res == m) {
            break;
        }
    }
    return res;
}

int flow(unordered_map<int, unordered_map<int, int> >& c, int s, int t) {
    unordered_map<int, unordered_map<int, int> > f;
    int h = 1 << 29;
    int r = 0;
    for (int i = 0; i < 30; ++i) {
        while (true) {
            pair<unordered_map<int, unordered_map<int, int>>, bool> res = bfs(f, h, c, s, t);
            if (res.second) {
                r += dfs(f, res.first, s, 1000000000, t);
            } else {
                break;
            }
        }
        h /= 2;
    }
    return r;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        auto [g, n] = inp();
        if (n != 1) {
            int result = flow(g, 0, -1);
            cout << result << '\n';
        }
    }
    return 0;
}
