n = int(raw_input())
p = [[0] * (len(bin(n)) - 2) for _ in range(n)]
d = [0] * n
for i in range(1, n):
    p[i][0] = int(raw_input()) - 1
    d[i] = d[p[i][0]] + 1

for j in range(1, len(p[0])):
    for i in range(1, n):
        p[i][j] = p[p[i][j - 1]][j - 1]

m = int(raw_input())
for _ in range(m):
    u, v = map(int, raw_input().split())
    u, v = u - 1, v - 1

    if d[u] > d[v]:
        u, v = v, u
    for i in range(len(p[0]) - 1, -1, -1):
        if d[p[v][i]] - d[u] >= 0:
            v = p[v][i]
    if u != v:
        for i in range(len(p[0]) - 1, -1, -1):
            if p[u][i] != p[v][i]:
                u = p[u][i]
                v = p[v][i]
        print p[u][0] + 1
    else:
        print u + 1
