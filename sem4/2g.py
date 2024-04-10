def inp():
    n = int(input())
    c = dict()
    for i in input().split():
        h = hash(i)
        c.setdefault(h, dict())[-h] = 1
        c.setdefault(-h, dict())[h] = 0
        c.setdefault(0, dict())[h] = 1
        c.setdefault(h, dict())[0] = 0
    if n == 1:
        print(0)
        return c, n
    for i in input().split():
        h = hash(i)
        c.setdefault(h, dict())[-h] = 1
        c.setdefault(-h, dict())[h] = 0
        c.setdefault(-h, dict())[-1] = 1
        c.setdefault(-1, dict())[-h] = 0
    for j in range(1, n - 1):
        for i in input().split():
            h = hash(i)
            c.setdefault(h, dict())[-h] = 1
            c.setdefault(-h, dict())[h] = 0
            c.setdefault(-h, dict())[j] = 1
            c.setdefault(j, dict())[-h] = 0
            c.setdefault(j, dict())[h] = 1
            c.setdefault(h, dict())[j] = 0
    return c, n

def flow(c, s, t):
    def bfs(f, h):
        g = dict()
        cur = {s}
        con = set()
        while cur:
            i = cur.pop()
            for j in set(c[i].keys()).difference(set(g.keys())):
                d = c[i][j] - f.setdefault(i, dict()).setdefault(j, 0)
                d -= d % h
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
    r = 0
    h = 2 ** 29
    for _ in range(30):
        while True:
            g, p = bfs(f, h)
            if p:
                r += dfs(f, g, s, 1e9)
            else:
                break
        h //= 2

    return f, r

for _ in range(int(input())):
    c, n = inp()
    if n == 1:
        continue
    f, r = flow(c, 0, -1)
    print(r)
