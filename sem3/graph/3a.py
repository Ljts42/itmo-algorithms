n, m = map(int, input().split())
g = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].add(b - 1)
    g[b - 1].add(a - 1)
 
e = [999999] * n
r = [999999] * n
v = [False] * n
b = [set() for _ in range(n)]
def dfs(i, p=-1):
    v[i] = True
    e[i] = 0 if p == -1 else e[p] + 1
    r[i] = 0 if p == -1 else e[p] + 1
    for j in g[i]:
        if j == p:
            continue
        if v[j]:
            r[i] = min(r[i], e[j])
        else:
            dfs(j, i)
            r[i] = min(r[i], r[j])
            if r[j] > e[i]:
                b[i].add(j)
                b[j].add(i)
 
for i in range(n):
    if not v[i]:
        dfs(i)
 
c = [-1] * n
 
def dfs2(i, t):
    c[i] = t
    for j in b[i]:
        if c[j] == -1:
            dfs2(j, t)
 
t = 0
for i in range(n):
    if c[i] == -1:
        dfs2(i, t)
        t += 1
 
k = [-1] * t
for i in range(n):
    k[c[i]] += 1
 
r = 0
for i in range(n):
    r += k[c[i]] - len(b[i])
 
print(r // 2)