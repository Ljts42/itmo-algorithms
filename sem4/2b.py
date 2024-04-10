def inp():
    n, m = map(int, input().split())
    c = dict()
    k = [[0] * n for _ in range(n)]
    for i in range(1, m + 1):
        x, y, z = map(int, input().split())
        c.setdefault(x, dict())
        c.setdefault(y, dict())
        c[x][y] = z
        c[y][x] = z
        k[x - 1][y - 1] = i
        k[y - 1][x - 1] = i
    return c, k

def flow(c, s, t):
    def bfs(f):
        g = dict()
        cur = {s}
        con = set()
        while cur:
            i = cur.pop()
            for j in set(c[i].keys()).difference(set(g.keys())):
                d = c[i][j] - max(0, f.setdefault(i, dict()).setdefault(j, 0))
                # d = c[i][j] - f.setdefault(i, dict()).setdefault(j, 0)
                if d > 0:
                    g.setdefault(i, dict())[j] = d
                    con.add(j)
            if len(cur) == 0:
                if t in con:
                    return g, True
                else:
                    cur = con
                    con = set()
        return g, False

    def dfs(f, g, i, m):
        if i == t:
            return m
        if i not in g:
            return 0
        r = 0
        for j in set(g[i].keys()):
            d = dfs(f, g, j, min(m - r, g[i][j]))
            r += d

            if d == 0 or g[i][j] == d:
                g[i].pop(j)
            else:
                g[i][j] -= d
            
            if d > 0:
                f[i][j] += d
                f.setdefault(j, dict()).setdefault(i, 0)
                f[j][i] -= d
            if r == m:
                break
        return r


    f = dict()
    while True:
        g, p = bfs(f)
        if p:
            dfs(f, g, s, 1000000000)
        else:
            break

    return f

c, k = inp()
f = flow(c, 1, len(k))
z = dict()
for i in f:
    for j in f[i]:
        if f[i][j] < 0:
            z.setdefault(i, dict())[j] = abs(f[i][j])
        elif f[i][j] < c[i][j]:
            z.setdefault(i, dict())[j] = c[i][j] - f[i][j]

v = set()

def res(i):
    v.add(i)
    for j in z.get(i, []):
        if j not in v:
            res(j)
res(1)
q = []
r = 0
for i in z:
    if i not in v:
        for j in z[i]:
            if j in v:
                r += z[i][j]
                q.append(k[i - 1][j - 1])
print(len(q), r)
print(*q)