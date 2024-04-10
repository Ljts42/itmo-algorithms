#include <bits/stdc++.h>

using namespace std;

void fft(vector<complex<double>> & a, bool inv) {
    if (a.size() == 1) return;

    vector<complex<double>> a0(a.size() / 2), a1(a.size() / 2);
    for (size_t i = 0; i < a.size() / 2; ++i) {
        a0[i] = a[i << 1];
        a1[i] = a[(i << 1) + 1];
    }
    fft(a0, inv);
    fft(a1, inv);

    complex<double> w(1);
    double ang = 2 * 3.141592653589793238463 / a.size() * (2 * inv - 1);
    complex<double> wn(cos(ang), sin(ang));
    for (size_t i = 0; i < a.size() / 2; ++i) {
        a[i] = a0[i] + w * a1[i];
        a[i + a.size() / 2] = a0[i] - w * a1[i];
        if (inv) {
            a[i] /= 2;
            a[i + a.size() / 2] /= 2;
        }
        w *= wn;
    }
}

void mul(vector<complex<double>> & a, vector<complex<double>> & b, vector<complex<double>> & c) {
    fft(a, false);
    fft(b, false);
    for (size_t i = 0; i < c.size(); ++i) {
        c[i] = a[i] * b[i];
    }
    fft(c, true);
}

void add(vector<complex<double>> & c) {
    // for (int i = c.size(); i >= 0; --i) {
    //     cout << round(c[i].real()) << ' ';
    // }

    vector<int> r(c.size(), 0);
    int k = 0;
    for (size_t i = 0; i < c.size(); ++i) {
        r[i] += round(c[i].real());
        if (r[i] > 0) {
            k = i;
            if (r[i] >= 10) {
                r[i + 1] += r[i] / 10;
                r[i] %= 10;
            }
        }
    }
    for (; k >= 0; --k) {
        cout << r[k];
    }
}

int main() {
    string x, y;
    cin >> x >> y;
    int n = 1;
    while (n < max(x.size(), y.size())) {
        n <<= 1;
    }
    n <<= 1;
    vector<complex<double>> a(n), b(n), c(n);
    bool inv = false;
    for (size_t i = 0; i < x.size(); ++i) {
        if (x[x.size() - i - 1] == '-') {
            inv = !inv;
            break;
        }
        a[i] = (x[x.size() - i - 1] - '0');
    }
    for (size_t i = 0; i < y.size(); ++i) {
        if (y[y.size() - i - 1] == '-') {
            inv = !inv;
            break;
        }
        b[i] = (y[y.size() - i - 1] - '0');
    }
    if ((x.size() == 1 && x[0] == '0')
            || (y.size() == 1 && y[0] == '0')) {
        cout << 0;
        return 0;
    } else if (inv) {
        cout << '-';
    }
    mul(a, b, c);
    add(c);
    
    return 0;
}