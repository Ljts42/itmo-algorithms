n, m = map(int, input().split())
p = [[i, 0] for i in range(n)]
r = [0] * n
z = {}


def find(x):
    s = p[x][1]
    mem = x
    while p[x][0] != x:
        x = p[x][0]
        s += p[x][1]
    # while p[mem][0] != mem:
    #     p[mem][0], mem = x, p[mem][0]
    return x, s

def union(x, y):
    x, _ = find(x)
    y, _ = find(y)
    if x == y:
        return
    if r[x] < r[y]:
        x, y = y, x
    p[y][0] = x
    p[y][1] -= p[x][1]
    if r[x] == r[y]:
        r[x] += 1


for _ in range(m):
    s = input().split()
    if s[0] == 'get':
        x, q = find(int(s[1]) - 1)
        print(q)
    elif s[0] == 'join':
        x, y = int(s[1]) - 1, int(s[2]) - 1
        union(x, y)
    else:
        x, v = int(s[1]) - 1, int(s[2])
        x, _ = find(x)
        p[x][1] += v
    # print(p)