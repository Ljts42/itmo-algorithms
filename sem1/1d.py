from random import randint as rnd


def func(x):
    n = len(a)
    p = 0
    for i in range(n):
        if x < a[i]:
            p += a[i]
        elif x <= b[i]:
            p += x
    return p


n = 20 # n = int(input())
a = []
b = []
s = []
for i in range(20):
    # x, y = map(int, input().split())
    x = rnd(1, 99)
    y = rnd(x + 1, 100)
    a.append(x)
    b.append(y)
    print(x, y)
    s.append([x, y])

res = [0, 0]
c = sorted(b)
d = sorted(s, key=lambda xx: [xx[1], xx[0]])
for i in c:
    p = func(i)
    if p >= res[1]:
        res = [i, p]
    else:
        break

print(*res, '\n')

for i in range(n):
    print(*d[i], func(d[i][1]))

# c = sorted(s, key=lambda x: [x[0], x[1]])
# d = sorted(s, key=lambda x: [x[1], x[0]])
# from random import randint as rnd
# for i in range(20):
#     x = rnd(1, 100)
#     y = rnd(x + 1, 100)
#     print(x, y)

