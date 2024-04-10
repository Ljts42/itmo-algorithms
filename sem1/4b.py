n, m = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= w[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + c[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
i, j = n, m
p = []
while dp[i][j] != 0:
    if dp[i][j] != dp[i - 1][j]:
        p.append(i)
        j -= w[i - 1]
    i -= 1
print(len(p))
print(*reversed(p))