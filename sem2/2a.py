n, m, a = map(int, input().split())

def genA(prev):
    return (23 * prev + 21563) % 16714589

def genUV(ind, p_u, p_v, p_r):
    return ((17 * p_u + 751 + p_r + 2 * ind) % n) + 1, \
           ((13 * p_v + 593 + p_r + 5 * ind) % n) + 1

st = [[999999999] * (len(bin(n + 1)) - 2) for _ in range(n)]
st[0][0] = a
for i in range(1, n):
    st[i][0] = genA(st[i - 1][0])

for j in range(1, len(st[0])):
    for i in range(n):
        st[i][j] = st[i][j - 1]
        if i + 2 ** (j - 1) < n:
            st[i][j] = min(st[i][j], st[i + 2 ** (j - 1)][j - 1])

u, v = map(int, input().split())

for i in range(1, m + 1):
    x, y = min(u, v), max(u, v)

    j = len(bin(y - x + 1)) - 3
    r = min(st[x - 1][j], st[y - 2 ** j][j])

    if i < m:
        u, v = genUV(i, u, v, r)

print(u, v, r)