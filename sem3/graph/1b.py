import sys
sys.setrecursionlimit(150000)

n, m, s, t = map(int, input().split())
s -= 1
t -= 1
g = [dict() for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if not (b - 1 in g[a - 1]):
        g[a - 1][b - 1] = c
    else:
        g[a - 1][b - 1] = min(g[a - 1][b - 1], c)

v = [False] * n
p = []
def dfs(i):
    v[i] = True
    for j in g[i]:
        if not v[j]:
            dfs(j)
    p.append(i)
dfs(s)
p.reverse()

r = [999999999] * n
r[s] = 0
for i in p:
    if r[i] == 999999999:
        continue
    for j in g[i]:
        r[j] = min(r[j], r[i] + g[i][j])
if r[t] == 999999999:
    print('Unreachable')
else:
    print(r[t])