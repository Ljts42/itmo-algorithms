def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


w, l = map(int, input().split())
n = int(input())
s = []
t = [1] * n
for i in range(n):
    s.append(list(map(int, input().split())))

x, y = map(int, input().split())

r = 0

while t.count(1) > 0:
    c, d = 9999, 9999
    j = -1
    for i in range(n):
        if t[i]:
            a, b = s[i]
            if dist(x, y, a, b) < dist(x, y, c, d):
                c, d = a, b
                j = i
    t[j] = 0

    if t.count(1) == n - 1:
        r += dist(x, y, c, d)
        x, y = c, d
    else:
        m1 = dist(x, y, -c, d)
        m2 = dist(x, y, c, -d)
        m3 = dist(x, y, 2 * w - c, d)
        m4 = dist(x, y, c, 2 * l - d)
        r += min(m1, m2, m3, m4)
        x, y = c, d

r += min(x, y, w - x, l - y)

print(r)