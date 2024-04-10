n = int(input())
s = list(map(lambda x: int(x) - 1, input().split()))
p = [[i, i] for i in range(n)]
r = [0] * n
z = [0] * n

def find(x):
    mem = x
    while p[x][0] != x:
        x = p[x][0]
    while p[mem][0] != mem:
        p[mem][0], mem = x, p[mem][0]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    p[y][0] = x
    p[x][1] = p[y][1]
    if r[x] == r[y]:
        r[x] += 1

q = [0] * n
for i in range(n):
    x = find(s[i])
    q[i] = p[x][1] + 1
    union(p[x][1], (p[x][1] + 1) % n)

print(*q)
