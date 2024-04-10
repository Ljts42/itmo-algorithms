n, m = map(int, input().split())
s = []
d = dict()
for i in range(n):
    s.append(input())
    d[s[-1]] = i

n *= 2
g = {i: set() for i in range(n)}
h = {i: set() for i in range(n)}

for _ in range(m):
    a, b = input().split(' => ')
    if a[0] == '+':
        a = d[a[1:]]
        a2 = a + n // 2
    else:
        a = d[a[1:]] + n // 2
        a2 = a - n // 2
    if b[0] == '+':
        b = d[b[1:]]
        b2 = b + n // 2
    else:
        b = d[b[1:]] + n // 2
        b2 = b - n // 2
    g[a].add(b)
    g[b2].add(a2)
    h[b].add(a)
    h[a2].add(b2)

v = [False] * n
c = [-1] * n
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
        if c[j] == -1:
            dfs2(j, k)

for i in range(n):
    if not v[i]:
        dfs(i)
j = 0
for i in reversed(p):
    if c[i] == -1:
        dfs2(i, j)
        j += 1

n //= 2
f = set()
for i in range(n):
    if c[i] == c[i + n]:
        f = set()
        break
    elif c[i] > c[i + n]:
        f.add(s[i])

if len(f) > 0:
    print(len(f))
    for i in f:
        print(i)
else:
    print(-1)