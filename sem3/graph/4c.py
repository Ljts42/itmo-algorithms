n, m = map(int, input().split())
s = list(map(int, input().split()))

r = 0
d = [(s[i] + s[0]) % m for i in range(n)]
d[0] = -1
for _ in range(n - 1):
    k = m
    i = 0
    for j in range(n):
        if d[j] != -1 and d[j] < k:
            k = d[j]
            i = j
    r += k
    for j in range(n):
        d[j] = min((s[i] + s[j]) % m, d[j])
    d[i] = -1

print(r)
