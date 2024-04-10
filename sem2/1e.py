import sys

sys.stdin = open('rmq.in')
sys.stdout = open('rmq.out', 'w')

def push(v):
    global MN, MX, minv, d, n
    if d[v] == MN:
        return

    if minv[v] == MX:
        minv[v] = d[v]
    else:
        minv[v] = max(d[v], minv[v])

    if v < n:
        d[2 * v] = max(d[v], d[2 * v])
        d[2 * v + 1] = max(d[v], d[2 * v + 1])

    d[v] = MN

def update(l, r, q, v, vl, vr):
    global MN, MX, minv, d, n
    push(v)
    if r <= vl or vr <= l:
        return
    if l <= vl and vr <= r:
        d[v] = q
        push(v)
        return
    
    vm = (vl + vr) // 2
    update(l, r, q, 2 * v, vl, vm)
    update(l, r, q, 2 * v + 1, vm, vr)
    
    minv[v] = min(minv[2 * v], minv[2 * v + 1])


def query(l, r, v, vl, vr):
    global MN, MX, minv, d, n
    push(v)
    if r <= vl or vr <= l:
        return MX
    if l <= vl and vr <= r:
        return minv[v]
 
    vm = (vl + vr) // 2
    return min(query(l, r, 2 * v, vl, vm),
               query(l, r, 2 * v + 1, vm, vr))


N, m = map(int, input().split())
n = 2 ** (len(bin(N - 1)) - 2)

inp = []

i, j, q = map(int, input().split())
inp.append([i - 1, j, q])

MN, MX = q - 1, q + 1

for _ in range(1, m):
    i, j, q = map(int, input().split())
    inp.append([i - 1, j, q])
    MN = min(MN, q - 1)
    MX = max(MX, q + 1)

minv = [MX for _ in range(2 * n)]
d = [MN for _ in range(2 * n)]


for l, r, q in inp:
    update(l, r, q, 1, 0, n)

for l, r, q in inp:
    if q != query(l, r, 1, 0, n):
        print('inconsistent')
        exit(0)

print('consistent')
for i in range(N):
    print(query(i, i + 1, 1, 0, n), end=" ")
