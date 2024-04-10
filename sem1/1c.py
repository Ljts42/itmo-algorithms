n = int(input())
a = list(map(int, input().split()))
s = [0] * n
for i in range(n):
    if a[i] < n:
        s[a[i]] += 1
for i in range(len(s) + 1):
    if i == len(s):
        print(i)
        break
    elif s[i] == 0:
        print(i)
        break
