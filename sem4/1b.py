for k in range(int(input())):
    if k != 0:
        print()

    n, m = map(int, input().split())
    g = {i: set(range(1, m + 1)) for i in range(1, n + 1)}
    for i in range(1, n + 1):
        g[i] -= set(map(int, input().split()[:-1]))

    p = dict()
    v = set()
    u = set()

    def dfs(i):
        if i not in v:
            v.add(i)
            for j in g[i]:
                if j not in p or dfs(p[j]):
                    p[j] = i
                    u.add(i)
                    return True
        return False

    for i in g:
        v = set()
        dfs(i)

    vl = set()
    vr = set(range(1, m + 1))

    def res(i):
        if i not in vl:
            vl.add(i)
            for j in g[i]:
                if j in p and p[j] != i:
                    if j in vr:
                        vr.discard(j)
                        res(p[j])

    for i in g:
        if i not in u:
            res(i)

    print(len(vl) + len(vr))
    print(len(vl), len(vr))
    print(*sorted(vl))
    print(*sorted(vr))