def zf(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(r - i, z[i - l]))
        while (i + z[i] < n) and (s[z[i]] == s[i + z[i]]):
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
        if r == len(s) and len(s) % l == 0:
            return l
    return n
s = input()
z = zf(s)
print(z)
