import sys

sys.stdin = open("hobbits.in")
sys.stdout = open("hobbits.out", 'w')

n = int(input())
g = dict()
for i in range(1, n + 1):
    g[i] = set()
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j]:
            g[i].add(j + 1)

v = set()

def rec(i):
    if i not in v:
        v.add(i)
        for j in g[i].copy():
            rec(j)
            g[i] |= g[j]

for i in g:
    rec(i)

p = dict()
v = set()
u = set()

def dfs(i):
    if i not in v:
        v.add(i)
        for j in g[i]:
            if j not in p or dfs(p[j]):
                p[j] = i
                u.add(i)
                return True
    return False

for i in g:
    v = set()
    dfs(i)

vl = set()
vr = set(range(1, n + 1))

def res(i):
    if i not in vl:
        vl.add(i)
        for j in g[i]:
            if j in p and p[j] != i:
                if j in vr:
                    vr.discard(j)
                    res(p[j])

for i in g:
    if i not in u:
        res(i)

r = vl.intersection(vr)
print(len(r))
print(*sorted(r))