#include <bits/stdc++.h>

using namespace std;

#define szof(x) ((int)x.size())

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        // int num;
        // cin >> num;
        // arr.push_back(num);
        cin >> arr[i];
    }

    for (int i = 0; i < n - 1; ++i) {
        if (arr[i] * 2 > arr[i + 1]) {
            cout << "No\n";
            return 0;
        }
    }

    // vector<vector<int>> field;
    vector<vector<int>> new_field(arr.back(), vector<int>(arr.back(), -1));

    int prev = 0;

    for (int i = 0; i < n; ++i) {
        // vector<vector<int>> new_field(arr[i], vector<int>(arr[i], -1));

        // for (int j = 0; j < prev; ++j) {
        //     for (int k = 0; k < prev; ++k) {
        //         new_field[j][k] = field[j][k];
        //     }
        // }

        for (int j = 0; j < arr[i] - prev; ++j) {
            for (int k = 0; k < prev; ++k) {
                new_field[prev + j][prev + (j + k) % (arr[i] - prev)] = k;
            }
        }

        vector<vector<int>> graph(arr[i]);
        vector<int> rl(arr[i], -1);
        vector<int> lr(arr[i], -1);

        for (int x = 0; x < arr[i]; ++x) {
            for (int y = 0; y < arr[i]; ++y) {
                if (new_field[x][y] == -1) {
                    graph[x].push_back(y);
                }
            }
        }

        vector<int> dist(arr[i]);
        vector<int> qu(arr[i]);
        vector<bool> used(arr[i]);
        vector<int> where(arr[i]);
        vector<int> vcnt(arr[i]);

        function<bool(int)> dfs = [&](int v) {
            while (vcnt[v] < szof(graph[v])) {
                int to = graph[v][vcnt[v]];
                if (rl[to] == -1 || (dist[rl[to]] == dist[v] + 1 && dfs(rl[to]))) {
                    // cerr << v << " " << to << endl;
                    lr[v] = to;
                    rl[to] = v;
                    where[v] = vcnt[v];
                    return true;
                }
                ++vcnt[v];
            }
            return false;
        };

        for (int j = prev; j < arr[i]; ++j) {
            // cerr << j << endl;
            fill(lr.begin(), lr.end(), -1);
            fill(rl.begin(), rl.end(), -1);
            while (true) {
                fill(dist.begin(), dist.end(), 1e9);
                fill(used.begin(), used.end(), 0);
                int l = 0, r = 0;
                for (int k = 0; k < arr[i]; ++k) {
                    if (lr[k] == -1) {
                        dist[k] = 0;
                        qu[r++] = k;
                        used[k] = true;
                    }
                }

                bool reached = false;
                while (l < r) {
                    int v = qu[l++];
                    for (int to : graph[v]) {
                        if (rl[to] == -1) {
                            reached = true;
                        } else if (!used[rl[to]]) {
                            dist[rl[to]] = dist[v] + 1;
                            qu[r++] = rl[to];
                            used[rl[to]] = true;
                        }
                    }
                }

                if (!reached) {
                    break;
                }

                fill(vcnt.begin(), vcnt.end(), 0);

                for (int k = 0; k < arr[i]; ++k) {
                    if (lr[k] == -1) {
                        dfs(k);
                    }
                }
            }

            for (int k = 0; k < arr[i]; ++k) {
                new_field[k][lr[k]] = j;
                swap(graph[k][where[k]], graph[k].back());
                graph[k].pop_back();
            }
        }

        prev = arr[i];
        // swap(field, new_field);
    }

    cout << "Yes\n";

    for (int i = 0; i < arr[n - 1]; ++i) {
        for (int j = 0; j < arr[n - 1]; ++j) {
            // cout << field[i][j] + 1 << " ";
            cout << new_field[i][j] + 1 << " ";
        }
        cout << "\n";
    }
}