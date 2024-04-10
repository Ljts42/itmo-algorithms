s = input()
n = len(s)
t = input()
m = len(t)
 
if n * m == 0:
    if n > m:
        print(n)
    else:
        print(m)
else:
    dp = [[999999999] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(m + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] - 1
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1], dp[i][j]) + 1
    print(dp[n][m])