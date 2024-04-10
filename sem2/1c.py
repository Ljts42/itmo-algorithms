import sys
 
inp = []
mn = sys.maxsize
mx = - sys.maxsize
 
for _ in range(int(input())):
    c, x, l = input().split()
    c, x, l = int(c == 'B'), int(x), int(l)
    inp.append([c, x, x + l])
    mn = min(mn, x)
    mx = max(mx, x + l)
 
mx -= mn
n = 2 ** (len(bin(mx - 1)) - 2)
 
left = [0] * 2 * n
right = [0] * 2 * n
length = [0] * 2 * n
count = [0] * 2 * n
 
def propogate(v):
    for i in (2 * v, 2 * v + 1):
        left[i] = left[v]
        right[i] = right[v]
        count[i] = count[v]
        length[i] = length[v] // 2
 
def segset(c, l, r, v = 1, vl = 0, vr = n):
    if r <= vl or vr <= l:
        return
    if l <= vl and vr <= r:
        left[v] = c
        right[v] = c
        count[v] = c
        length[v] = (vr - vl) * c
        return
 
    if length[v] == 0 or length[v] == vr - vl:
        propogate(v)
    vm = (vl + vr) // 2
 
    segset(c, l, r, 2 * v, vl, vm)
    segset(c, l, r, 2 * v + 1, vm, vr)
 
    left[v] = left[2 * v]
    right[v] = right[2 * v + 1]
    count[v] = count[2 * v] + count[2 * v + 1] - (right[2 * v] * left[2 * v + 1])
    length[v] = length[2 * v] + length[2 * v + 1]
 
for c, l, r in inp:
    segset(c, l - mn, r - mn)
    print(count[1], length[1])
