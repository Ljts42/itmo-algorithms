n = int(input())
s = []
for i in range(n):
    x, y = map(int, input().split())
    s.append([x, y])

r = 0
d = [(s[i][0] - s[0][0]) ** 2 + (s[i][1] - s[0][1]) ** 2 for i in range(n)]
for _ in range(n - 1):
    m = 999999999
    i = 0
    for j in range(n):
        if d[j] != 0 and d[j] < m:
            m = d[j]
            i = j
    r += m ** (1 / 2)
    for j in range(n):
        d[j] = min((s[i][0] - s[j][0]) ** 2 + (s[i][1] - s[j][1]) ** 2, d[j])

print(r)
