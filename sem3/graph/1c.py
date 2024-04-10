n = int(input())
s = [['*' if ((i%2==j%2) or (i == n//2) or (j == n//2)) else '.' for j in range(n)] for i in range(n)]
for i in s:
  print(*i)