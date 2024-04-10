from collections import deque

n = int(input())
k = int(input())
e = set(map(int, input().split()))

m = int(input())
g = [set() for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

d = [999999999] * (n + 1)
p = [999999999] * (n + 1)
q = deque(sorted(e))
for i in e:
    d[i] = 0
    p[i] = i

while q:
    i = q.popleft()
    for j in g[i]:
        if d[i] + 1 < d[j]:
            d[j] = d[i] + 1
            p[j] = p[i]
            q.append(j)
        elif d[i] + 1 == d[j] and p[i] < p[j]:
            p[j] = p[i]
            q.append(j)

print(*d[1:])
print(*p[1:])
