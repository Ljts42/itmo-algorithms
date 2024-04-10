n, m, k = map(int, input().split())
p = [i for i in range(n)]
r = [0] * n
 
def find(x):
    mem = x
    while p[x] != x:
        x = p[x]
    while p[mem] != mem:
        p[mem], mem = x, p[mem]
    return x
 
def union(x, y):
    x = find(x)
    y = find(y)
    if r[x] < r[y]:
        x, y = y, x
    p[y] = x
    if r[x] == r[y]:
        r[x] += 1


for _ in range(m):
    input()

z = [0] * k
q = []
for i in range(k):
    s, x, y = input().split()
    z[i] = [s, int(x) - 1, int(y) - 1]

for i in range(k - 1, -1, -1):
    if z[i][0] == 'ask':
        if find(z[i][1]) == find(z[i][2]):
            q.append('YES')
        else:
            q.append('NO')
    else:
        union(z[i][1], z[i][2])
print(*reversed(q), sep='\n')