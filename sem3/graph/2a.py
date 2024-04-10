import sys
sys.setrecursionlimit(100000)

n = int(input())
m = int(input())
g = {i: set() for i in range(1, n + 1)}
h = {i: set() for i in range(1, n + 1)}
 
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    h[b].add(a)
 
v = [False] * (n + 1)
c = [0] * (n + 1)
p = []
 
def dfs(i):
    v[i] = True
    for j in g.get(i, []):
        if not v[j]:
            dfs(j)
    p.append(i)
 
def dfs2(i, k):
    c[i] = k
    for j in h.get(i, []):
        if c[j] == 0:
            dfs2(j, k)
 
for i in range(1, n + 1):
    if not v[i]:
        dfs(i)
j = 1
for i in reversed(p):
    if c[i] == 0:
        dfs2(i, j)
        j += 1
 
t = [True] * j
for i in g:
    for j in g[i]:
        if c[i] != c[j]:
            t[c[i]] = False
 
v = set()
r = set()
for i in range(1, n + 1):
    if t[c[i]] and not c[i] in v:
        v.add(c[i])
        r.add(i)
 
print(len(r))
print(*r)