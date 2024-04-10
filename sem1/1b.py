r, c = map(int, input().split())
s = []
for i in range(r * c):
    s.append(int(input()))
s.sort()
m = 0
for i in range(r):
    m = max(m, s[i * c + c - 1] - s[i * c])
print(m)
