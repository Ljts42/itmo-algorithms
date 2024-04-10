n = int(input())
s = [0] * (n + 1)
for i in range(2, n + 1):
    z = set()
    for j in range(i):
        z.add(s[j] ^ s[i - j - 1])
    k = 0
    while True:
        if not k in z:
            s[i] = k
            break
        k += 1

if s[n] == 0:
    print('Mueller')
else:
    print('Schtirlitz')
    r = []
    for i in range(n):
        if s[i] ^ s[n - i - 1] == 0:
            r.append(i + 1)
    print(*r)
