import sys

sys.stdin = open("assignment.in")
sys.stdout = open("assignment.out", 'w')

n = int(input())
s = [[10000000] * (n + 1)]
for _ in range(n):
    s.append([10000000] + list(map(int, input().split())))

u = [0] * (n + 1)
v = [0] * (n + 1)
p = [0] * (n + 1)

way = [0] * (n + 1)

for i in range(1, n + 1):
    p[0] = i
    j0 = 0
    minv = [10000000] * (n + 1)
    vis = set()
    while True:
        vis.add(j0)
        i0 = p[j0]
        d = 10000000
        j1 = 0
        for j in set(range(1, n + 1)).difference(vis):
            if s[i0][j] - u[i0] - v[j] < minv[j]:
                minv[j] = s[i0][j] - u[i0] - v[j]
                way[j] = j0
            if minv[j] < d:
                d = minv[j]
                j1 = j
        for j in range(0, n + 1):
            if j in vis:
                u[p[j]] += d
                v[j] -= d
            else:
                minv[j] -= d
        j0 = j1
        if p[j0] == 0:
            break
    while True:
        p[j0] = p[way[j0]]
        j0 = way[j0]
        if j0 == 0:
            break

print(-v[0])
for i in range(1, n + 1):
    print(p[i], i)