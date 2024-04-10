n = int(input())
s = sorted(map(int, input().split()))
k = int(input())
res = [0] * k
for i in range(k):
    a, b = map(int, input().split())

    l1 = -1
    r1 = len(s)
    while r1 - l1 > 1:
        m1 = (l1 + r1) // 2
        if s[m1] < a:
            l1 = m1
        else:
            r1 = m1

    l2 = -1
    r2 = len(s)
    while r2 - l2 > 1:
        m2 = (r2 + l2) // 2
        if s[m2] <= b:
            l2 = m2
        else:
            r2 = m2

    if r1 == l2:
        res[i] = 1
    else:
        res[i] = - r1 + l2 + 1

print(*res)
