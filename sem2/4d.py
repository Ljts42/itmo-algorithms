n, k = map(int, input().split())
s = list(map(int, input().split()))
def prov(x):
    cows = 1
    last = s[0]
    for c in s:
        if c - last >= x:
            cows += 1
            last = c
    return cows >= k
l = 0
r = s[n - 1] - s[0] + 1
while r - l != 1:
    m = (l + r) // 2
    if prov(m):
        l = m
    else:
        r = m
print(l)
