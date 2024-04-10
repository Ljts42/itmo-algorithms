def kar(x, y):
    if x <= 1e9 or y <= 1e9:
        return x * y
    
    n = (max(len(str(x)), len(str(y))) + 1) // 2
    xr, xl = divmod(x, 10 ** n)
    yr, yl = divmod(y, 10 ** n)
    z0 = kar(xl, yl)
    z1 = kar((xl + xr), (yl + yr))
    z2 = kar(xr, yr)
    return (z2 * 10 ** (2 * n)) + ((z1 - z2 - z0) * 10 ** n) + z0

print(kar(int(input()), int(input())))

# a = input()
# b = input()
# neg = (a[0] == '-') ^ (b[0] == '-')

# if a[0] == '-':
#     a = a[1:]
# if b[0] == '-':
#     b = b[1:]

# a = list(reversed(list(map(int, a))))
# b = list(reversed(list(map(int, b))))

# def mul(x, y):
#     q = [0] * (len(x) + len(y))
#     z = 0
#     for i in range(len(q)):
#         for j in range(min(i + 1, len(x))):
#             if i - j < len(y):
#                 add(q, [x[j] * y[i-j]], i)
#             # q[i] += x[j] * y[i-j]
#         if q[i] != 0:
#             z = i + 1
#     return q[:z]

# def add(x, y, s=0):
#     x += [0] * (s + 1 - len(x))
#     for i in range(len(y)):
#         if s + i >= len(x):
#             x.append(y[i])
#         else:
#             x[s + i] += y[i]
#             if x[s + i] >= 10:
#                 x.append(1)
#                 x[s + i] -= 10
#     return x

# def sub(x, y, s=0):
#     if len(x) < len(u)


# def car(x, y):
#     if len(x) <= 100 and len(y) <= 100:
#         return mul(x, y)

#     n = (min(len(x), len(y)) + 1) // 2
#     # m = len(y) // 2 + 1
#     xl, xr = x[:n], x[n:]
#     yl, yr = y[:n], y[n:]

#     r1 = car(xr, yr)
#     r2 = car(add(xl, xr), add(yl, yr))
#     r3 = car(xl, yl)
#     s, f = sub(r2, r1)
#     z = add(r3, r1, 2 * n)
#     if f:
#         s = add(s, r3)
#     else:
#         s, f = sub(s, r3)

#     if f:
#         res, f = sub(z, s, n)
#         neg ^= f
#         return res
#     else:
#         return add(z, s, n)