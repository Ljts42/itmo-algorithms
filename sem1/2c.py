n, L = map(int, input().split())

s = sorted(map(int, input().split()))


def prov(x):
    i = 0
    m = 0
    while i < n - 1:
        if s[i] <= m + x:
            if m + x < s[i + 1]:
                m += x
            else:
                m = s[i + 1] - 0.000001
            i += 1
        else:
            return False
    return L <= m + x


l = 0.
r = L
while r - l > 0.000001:
    m = (l + r) / 2
    if prov(m):
        r = m
    else:
        l = m
if prov(l):
    print(l)
else:
    print(r)
