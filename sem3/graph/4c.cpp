#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    long long n, M;
    cin >> n >> M;
    vector<long long> s(n), d(n);
    for (long long i = 0; i < n; ++i) {
        cin >> s[i];
        d[i] = (s[i] + s[0]) % M;
    }
    d[0] = -1;
    long long r = 0;
    for (long long k = 1; k < n; ++k) {
        long long m = M, i = 0;
        for (long long j = 0; j < n; ++j) {
            if (d[j] != -1 && d[j] < m) {
                m = d[j];
                i = j;
            }
        }
        r += m;
        for (long long j = 0; j < n; ++j) {
            d[j] = min((s[i] + s[j]) % M, d[j]);
        }
        d[i] = -1;
    }
    cout << r;
}
