def inp():
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(1, n):
        if s[i - 1] * 2 > s[i]:
            print('No')
            return []
    print('Yes')
    return s


def init(r, x, y):
    g = {i: dict() for i in range(y * 2 + 2)}
    for i in range(1, y + 1):
        g[0][i] = 1
        g[i][0] = 0
        g[y + i][y * 2 + 1] = 1
        g[y * 2 + 1][y + i] = 1
    for i in range(x, y):
        for j in range(x):
            r[i][x + (i + j) % (y - x)] = j + 1
            g[i + 1][y + j + 1] = 1000000000
            g[y + j + 1][i + 1] = 0
            g[j + 1][y + i + 1] = 1000000000
            g[y + i + 1][j + 1] = 0
        for j in range(x, y):
            if r[i][j] == 0:
                g[i + 1][y + j + 1] = 1000000000
                g[y + j + 1][i + 1] = 0
    return g


def bfs(f, h, c, s, t):
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


def dfs(f, g, i, m, t):
    if i == t or m == 0:
        return m
    if i not in g:
        return 0
    r = 0
    for j in set(g[i].keys()):
        d = dfs(f, g, j, min(m - r, g[i][j]), t)
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


def flow(c, s, t):
    f = dict()

    h = 2 ** 30
    for _ in range(30):
        h //= 2
        while True:
            g, p = bfs(f, h, c, s, t)
            if p:
                dfs(f, g, s, 1000000000, t)
            else:
                break


    return f


def solve(a):
    r = [[0] * a[-1] for _ in range(a[-1])]
    for i in range(a[0]):
        for j in range(a[0]):
            r[i][j] = (i + j) % a[0] + 1

    for k in range(1, len(a)):
        g = init(r, a[k - 1], a[k])
        for n in range(a[k - 1] + 1, a[k] + 1):
            f = flow(g, 0, a[k] * 2 + 1)
            for i in range(1, a[k] + 1):
                for j in range(1, a[k] + 1):
                    if f.get(i, dict()).get(a[k] + j, 0) == 1:
                        r[i - 1][j - 1] = n
                        g[i].pop(a[k] + j, 0)
                        g[a[k] + j].pop(i, 0)
                        break
    return r


a = inp()
if a:
    for i in solve(a):
        print(*i)