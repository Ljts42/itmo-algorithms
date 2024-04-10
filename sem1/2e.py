n, a, b, w, h = map(int, input().split())
def prov(d):
    f = (w // (a + 2 * d)) * (h // (b + 2 * d))
    f = max(f, (w // (b + 2 * d)) * (h // (a + 2 * d)))
    if f >= n:
        return True
    else:
        return False
l, r = 0, 10 ** 18
while r - l > 1:
    m = (r + l) // 2
    if prov(m):
        l = m
    else:
        r = m
if prov(r):
    print(r)
else:
    print(l)
