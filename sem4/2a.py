n = int(input())
m = int(input())

g = [[] for _ in range(n)]
e = []
for i in range(m):
    a, b, c = map(int, input().split())
    e.append([b - 1, c, 0, 2 * i + 1])
    g[a - 1].append(e[-1])
    e.append([a - 1, c, 0, 2 * i])
    g[b - 1].append(e[-1])

v = set()

def dfs(i, s):
    if i == n - 1:
        return s
    v.add(i)
    for j in range(len(g[i])):
        if g[i][j][0] not in v and g[i][j][1] > g[i][j][2]:
            d = dfs(g[i][j][0], min(g[i][j][1] - g[i][j][2], s))
            if d > 0:
                g[i][j][2] += d
                e[g[i][j][3]][2] -= d
                return d
    return 0

r = 0
f = 1
while f:
    v = set()
    f = dfs(0, 1e9)
    r += f

print(r)
for i in e[::2]:
    print(i[2])