n = int(input())
r = []
for i in range(n + 1):
    r.append([])
    for j in range(n):
        r[-1].append(int(input()))
d = []
for i in range(n):
    d.append([])
    for j in range(n + 1):
        d[-1].append(int(input()))
l = []
for i in range(n + 1):
    l.append([])
    for j in range(n):
        l[-1].append(int(input()))
u = []
for i in range(n):
    u.append([])
    for j in range(n + 1):
        u[-1].append(int(input()))
# r = [[0] * n for _ in range(n + 1)]
# for i in range(n):
#     for j in range(n + 1):
#         r[j][i] = int(input())
# d = [[0] * (n + 1) for _ in range(n)]
# for i in range(n + 1):
#     for j in range(n):
#         d[j][i] = int(input())
# l = [[0] * n for _ in range(n + 1)]
# for i in range(n):
#     for j in range(n + 1):
#         l[j][i] = int(input())
# u = [[0] * (n + 1) for _ in range(n)]
# for i in range(n + 1):
#     for j in range(n):
#         u[j][i] = int(input())

g = dict()
g[0] = dict()
for i in range(n):
    g[0][i * n + 1] = min(g[0].get(i * n + 1, 1e9), d[i][0])
    g[0][n * n - n + i + 1] = min(g[0].get(n * n - n + i + 1, 1e9), r[-1][i])

    g.setdefault(i + 1, dict())
    g[i + 1][n * n + 1] = min(g[i + 1].get(n * n + 1, 1e9), r[0][i])

    g.setdefault(i * n + n, dict())
    g[i * n + n][n * n + 1] = min(g[i * n + n].get(n * n + 1, 1e9), d[i][-1])

for i in range(n):
    for j in range(n):
        g.setdefault(i * n + j + 1, dict())
        if i != 0:
            g[i * n + j + 1][(i - 1) * n + j + 1] = min(g[i * n + j + 1].get((i - 1) * n + j + 1, 1e9), r[i][j])
        if i != n - 1:
            g[i * n + j + 1][(i + 1) * n + j + 1] = min(g[i * n + j + 1].get((i + 1) * n + j + 1, 1e9), l[i + 1][j])
        if j != 0:
            g[i * n + j + 1][i * n + j] = min(g[i * n + j + 1].get(i * n + j, 1e9), u[i][j])
        if j != n - 1:
            g[i * n + j + 1][i * n + j + 2] = min(g[i * n + j + 1].get(i * n + j + 2, 1e9), d[i][j + 1])

def dij():
    m = [1e9] * (n * n + 2)
    m[0] = 0
    v = set()
    for i in g:
        k = -1
        for j in g:
            if (j not in v) and (k == -1 or m[j] < m[k]):
                k = j
        if k == -1 or k == n * n + 1:
            break
        v.add(k)
        for j in g.get(k, []):
            if m[k] + g[k].get(j, 1e9) < m[j]:
                m[j] = m[k] + g[k][j]
    return m[-1]

print(dij())