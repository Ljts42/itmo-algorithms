import sys

n = 2 ** (len(bin(int(input()) - 1)) - 2)
tree = [0] * n + list(map(int, input().split()))
tree += [0] * (2 * n - len(tree))

for i in range(n - 1, -1, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

def set(pos, val):
    v = pos + n
    tree[v] = val
    while v != 1:
        v //= 2
        tree[v] = tree[v * 2] + tree[v * 2 + 1]

def get(v, vl, vr, l, r):
    if vr <= l or r <= vl:
        return 0
    if l <= vl and vr <= r:
        return tree[v]

    vm = (vl + vr) // 2
    return get(v * 2, vl, vm, l, r) + get(v * 2 + 1, vm, vr, l, r)

for op in sys.stdin:
    op, i, j = op.split()
    i, j = int(i), int(j)
    if op == 'set':
        set(i - 1, j)
    else:
        print(get(1, 0, n, i - 1, j))
