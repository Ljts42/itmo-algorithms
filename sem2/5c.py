import sys
 
sys.setrecursionlimit(1000000000)
 
n = int(raw_input())
d = dict()
for _ in range(n - 1):
    a, b = map(int, raw_input().split())
    d.setdefault(a, set())
    d[a].add(b)
 
v = [0] * (n + 1)
q = set(d.keys())
 
def func(u):
    if not v[u]:
        v[u] = True
        for i in d.get(u, set()).copy():
            d[u] |= func(i)
    return d.get(u, set())
 
for i in q:
    func(i)
 
m = int(raw_input())
for _ in range(m):
    x, y = map(int, raw_input().split())
    if x == y or (y in d.get(x, set())):
        print 'Yes'
    else:
        print 'No'