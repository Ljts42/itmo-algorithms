n, m = map(int, input().split())
s = list(map(int, input().split()))
r = []
for i in range(n // 2, -1, -1):
    f = True
    for j in range(i):
        if s[i + j] != s[i - j - 1]:
            f = False
            break
    if f:
        r.append(n - i)
print(*r)
