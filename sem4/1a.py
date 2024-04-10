def inp():
    n, m = map(int, input().split())
    c = dict()
    for i in range(1, n + 1):
        c.setdefault(0, dict())[i] = 1
        # c.setdefault(i, dict())[0] = 1
        c.setdefault(i, dict())[0] = 0
    for i in range(n + 1, n + m + 1):
        c.setdefault(i, dict())[n + m + 1] = 1
        # c.setdefault(n + m + 1, dict())[i] = 1
        c.setdefault(n + m + 1, dict())[i] = 0
    for i in range(1, n + 1):
        for j in map(int, input().split()[:-1]):
            c.setdefault(i, dict())[j + n] = 1e9
            # c.setdefault(j + n, dict())[i] = 1e9
            c.setdefault(j + n, dict())[i] = 0
    return c, n, m

def flow(c, s, t):
    def bfs(f):
        g = dict()
        cur = {s}
        con = set()
        while cur:
            i = cur.pop()
            for j in set(c[i].keys()).difference(set(g.keys())):
                # d = c[i][j] - max(0, f.setdefault(i, dict()).setdefault(j, 0))
                # d = c[i][j] - f.setdefault(i, dict()).setdefault(j, 0)
                d = -f.setdefault(i, dict()).setdefault(j, 0)
                if f[i][j] >= 0:
                    d += c[i][j]
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
        if i == t or m == 0:
            return m
        if i not in g:
            return 0
        r = 0
        for j in set(g[i].keys()):
            d = dfs(f, g, j, min(m - r, g[i][j]))
            # d = dfs(f, g, j, min(m, g[i][j]))
            r += d

            if d == 0 or g[i][j] == d:
                g[i].pop(j)
            else:
                g[i][j] -= d
            
            if d > 0:
                f[i][j] += d
                f.setdefault(j, dict()).setdefault(i, 0)
                f[j][i] -= d
                # return d
            if r == m:
                break
        return r
        # return 0

    f = dict()
    r = 0
    while True:
        g, p = bfs(f)
        if p:
            r += dfs(f, g, s, 1e9)
        else:
            break

    return f, r

c, n, m = inp()
f, r = flow(c, 0, n + m + 1)
print(r)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if f.get(i, dict()).get(j + n, 0) == 1:
            print(i, j)