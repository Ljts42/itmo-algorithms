import sys
sys.setrecursionlimit(2**30)

def inp():
    n, l, h, m = map(int, input().split())
    s = list(map(int, input().split()))
    c = dict()
    # for i in range(1, h + 1):
    for i in range(1, l):
        c.setdefault(0, dict())[i] = 1000000000
        c.setdefault(i, dict())[0] = 0
    # for i in range(l, n + 1):
    for i in range(h + 1, n + 1):
        c.setdefault(i, dict())[n + 1] = 1000000000
        c.setdefault(n + 1, dict())[i] = 0
    for i in range(1, m):
        if s[i - 1] != s[i]:
            # c.setdefault(s[i - 1], dict())[s[i]] = 1
            c.setdefault(s[i - 1], dict()).setdefault(s[i], 1)
            # c[s[i - 1]][s[i]] += 1
            # c.setdefault(s[i], dict())[s[i - 1]] = 0
            c.setdefault(s[i], dict()).setdefault(s[i - 1], 0)
            # c[s[i - 1]][s[i]] += 1
    return c, n

def flow(c, s, t):
    def bfs(f):
        p = [False] * 1010
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
                # elif f[i][j] == 1000000000:
                #     continue
                if d > 0:
                    g.setdefault(i, dict())[j] = d
                    con.add(j)
                    if p[i] or d == 1:
                        p[j] = True
            if len(cur) == 0:
                if t in con:
                    return g, p[t]
                else:
                    cur = con
                    con = set()
        return g, p[t]

    def dfs(f, g, i, m):
        if i == t or m == 0:
            if m >= 1000000:
                return 0
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
    # r = 0
    while True:
        g, p = bfs(f)
        if p:
            # r += dfs(f, g, s, 1000000000)
            if dfs(f, g, s, 1000000000) == 0:
                break
        else:
            break

    return f

def dfs(c, f, t, v, i, m):
    if i == t:
        return m
    if i not in c:
        return 0
    v.add(i)
    for j in c[i]:
        if j not in v and c[i][j] > f.setdefault(i, dict()).setdefault(j, 0):
            d = -f[i][j]
            if f[i][j] >= 0:
                d += c[i][j]
            d = dfs(c, f, t, v, j, min(d, m))
            if d > 0:
                f[i][j] += d
                f.setdefault(j, dict()).setdefault(i, 0)
                f[j][i] -= d
                return d
    return 0


c, n = inp()
f = dict()
v = set()
b = 0
while True:
    a = dfs(c, f, n + 1, v, 0, 1000000000)
    if a == 0:
        break
    b += a
    v = set()


# f = flow(c, 0, n + 1)
r = 0
for i in range(1, n + 1):
    for j in f.get(i, []):
        # if 1 <= j <= n and (20 <= j <= 80 or 20 <= i <= 80) and f[i][j] > 0:
        if 1 <= j <= n and f[i][j] > 0:
            r += f[i][j]
print(r)
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if f.get(i, dict()).get(j + n, 0) == 1:
#             print(i, j)



# 2 27 3 53 53 52 52 60 85 89 100 53 60 2 3 53 100 89 40 42 2 53 2 85
# b    b                a  a  a         b b    a   a        b    b a
# b a  b                a  a  a         b b    a   a        b    b a
