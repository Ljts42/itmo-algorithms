#include <bits/stdc++.h>

using namespace std;

size_t p[2023], d[2023], s[1010], r[1010][1010];

bool dfs(vector<vector<size_t>>& g, size_t i) {
    // for (size_t j : g[i]) {
    for (size_t j = 0; j < g[i].size(); ++j) {
        // if (p[j] == -1 || d[p[j]] == d[i] + 1 && dfs(g, p[j])) {
        if (p[g[i][j]] == -1 || (d[p[g[i][j]]] == d[i] + 1 && dfs(g, p[g[i][j]]))) {
            // p[j] = i;
            p[g[i][j]] = i;
            // p[i] = j;
            p[i] = g[i][j];
            swap(g[i][j], g[i].back());
            return true;
        }
    }
    // d[i] = 1e9;
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    size_t n;
    cin >> n;
    // vector<size_t> s(n);
    for (size_t i = 0; i < n; ++i) {
        cin >> s[i];
    }

    for (size_t i = 0; i < n - 1; ++i) {
        if (s[i] * 2 > s[i + 1]) {
            cout << "No\n";
            return 0;
        }
    }
    cout << "Yes\n";

    // vector<vector<size_t>> r(s[n - 1], vector<size_t>(s[n - 1]));
    queue<size_t> q;

    for (size_t i = 0; i < s[0]; ++i) {
        for (size_t j = 0; j < s[0]; ++j) {
            r[i][j] = (i + j) % s[0] + 1;
        }
    }

    for (size_t k = 0; k + 1 < n; ++k) {
        vector<vector<size_t>> g(2 * s[k + 1]);

        for (size_t i = s[k]; i < s[k + 1]; ++i) {
            for (size_t j = 0; j < s[k]; ++j) {
                r[i][s[k] + (i + j) % (s[k + 1] - s[k])] = j + 1;

                g[i].push_back(s[k + 1] + j);
                // g[s[k] + j].push_back(i);
                g[j].push_back(s[k + 1] + i);
                // g[s[k] + i].push_back(j);
            }

            for (size_t j = s[k]; j < s[k + 1]; ++j) {
                if (r[i][j] == 0) {
                    g[i].push_back(s[k + 1] + j);
                    // g[s[k] + j].push_back(i);
                }
            }
        }

        // for (size_t i = s[k - 1]; i < s[k]; ++i) {
        //     for (size_t j = 0; j < s[k - 1]; ++j) {
        //         r[i][s[k - 1] + (i + j) % (s[k] - s[k - 1])] = j + 1;
        //     }
        // }
        // vector<vector<size_t>> g(2 * s[k]);
        // for (size_t i = 0; i < s[k]; ++i) {
        //     for (size_t j = 0; j < s[k]; ++j) {
        //         if (r[i][j] == 0) {
        //             g[i].push_back(s[k] + j);
        //             // g[j + s[k - 1]].push_back(i);
        //             // g[i].push_back(j);
        //         }
        //     }
        // }

        for (size_t m = s[k] + 1; m <= s[k + 1]; ++m) {
            // vector<size_t> p(2 * s[k], -1);
            // vector<size_t> d(2 * s[k], 1e9);
            for (size_t i = 0; i < 2 * s[k + 1]; ++i) {
                p[i] = -1;
                // d[i] = 1e9;
            }

            while (true) {
                for (size_t i = 0; i < s[k + 1]; ++i) {
                    if (p[i] == -1) {
                        d[i] = 0;
                        q.push(i);
                    } else {
                        d[i] = 1e9;
                    }
                }

                bool f = false;
                while (!q.empty()) {
                    size_t i = q.front();
                    q.pop();
                    for (size_t j : g[i]) {
                        if (p[j] == -1) {
                            f = true;
                        } else if (d[p[j]] == 1e9) {
                            d[p[j]] = d[i] + 1;
                            q.push(p[j]);
                        }
                    }
                }
                if (!f) break;

                for (size_t i = 0; i < s[k + 1]; ++i) {
                    if (p[i] == -1) {
                        dfs(g, i);
                    }
                }
            }

            for (size_t i = 0; i < s[k + 1]; ++i) {
                r[i][p[i] - s[k + 1]] = m;
                g[i].pop_back();
                // g[i].erase(p[i]);
                // g[p[i]].erase(i);
            }
        }
    }

    for (size_t i = 0; i < s[n - 1]; ++i) {
        for (size_t j = 0; j < s[n - 1]; ++j) {
            std::cout << r[i][j] << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}