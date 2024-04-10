n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(int(input()))
 
l, r = 0, 10000000
 
result = 1
 
if sum(s) <= k:
    if sum(s) == k:
        print(1)
    else:
        print(0)
else:
    while l <= r:
        m = (l + r) // 2
        p = 0
        for i in range(n):
            p += s[i] // m
            if p >= k:
                break
        if p >= k:
            l = m + 1
            result = max(result, m)
        else:
            r = m - 1
 
    print(result)