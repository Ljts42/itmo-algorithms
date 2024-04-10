import sys

n = 2 ** (len(bin(int(input()) - 1)) - 2)

minv = [sys.maxsize] * 2 * n
addv = [0] * 2 * n
setv = [None] * 2 * n

a = list(map(int, input().split()))
for i in range(len(a)):
    minv[i + n] = a[i]

for i in range(n - 1, 0, -1):
    minv[i] = min(minv[i * 2], minv[i * 2 + 1])

def propogate(v):
    if setv[v] != None:
        minv[2 * v] = setv[v]
        minv[2 * v + 1] = setv[v]
        addv[2 * v] = 0
        addv[2 * v + 1] = 0
        setv[2 * v] = setv[v]
        setv[2 * v + 1] = setv[v]
        setv[v] = None

    if addv[v] != 0:
        addv[2 * v] += addv[v]
        addv[2 * v + 1] += addv[v]
        addv[v] = 0

def segset(l, r, val, v = 1, vl = 0, vr = n):
    if r <= vl or vr <= l:
        return
    if l <= vl and vr <= r:
        minv[v] = val
        addv[v] = 0
        setv[v] = val
        return

    propogate(v)
    vm = (vl + vr) // 2
    
    segset(l, r, val, 2 * v, vl, vm)
    segset(l, r, val, 2 * v + 1, vm, vr)
    
    minv[v] = min(minv[2 * v] + addv[2 * v],
                  minv[2 * v + 1] + addv[2 * v + 1])

def segadd(l, r, val, v = 1, vl = 0, vr = n):
    if r <= vl or vr <= l:
        return
    if l <= vl and vr <= r:
        addv[v] += val
        return
    
    propogate(v)
    vm = (vl + vr) // 2
    
    segadd(l, r, val, 2 * v, vl, vm)
    segadd(l, r, val, 2 * v + 1, vm, vr)

    minv[v] = min(minv[2 * v] + addv[2 * v],
                  minv[2 * v + 1] + addv[2 * v + 1])

def getmin(l, r, v = 1, vl = 0, vr = n):
    if r <= vl or vr <= l:
        return sys.maxsize
    if l <= vl and vr <= r:
        return minv[v] + addv[v]
    
    propogate(v)
    minv[v] = min(minv[2 * v] + addv[2 * v],
                  minv[2 * v + 1] + addv[2 * v + 1])
    vm = (vl + vr) // 2
    return min(getmin(l, r, 2 * v, vl, vm),
               getmin(l, r, 2 * v + 1, vm, vr))

for op in sys.stdin:
    op = op.split()
    if op[0] == 'min':
        op, i, j = op
        print(getmin(int(i) - 1, int(j)))
    else:
        i, j, k = int(op[1]) - 1, int(op[2]), int(op[3])
        if op[0] == 'set':
            segset(i, j, k)
        elif op[0] == 'add':
            segadd(i, j, k)
