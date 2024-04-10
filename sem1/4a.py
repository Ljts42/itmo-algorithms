f = open('muggers.in')
# n, k = map(int, input().split())
n, k = map(int, f.readline().split())
k += 1
s = list(map(int, f.readline().split()))
f.close()
dp = [999999999] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + s[i - 1]
    for j in range(2, min(i + 1, k + 1)):
        dp[i] = min(dp[i], dp[i - j] + s[i - 1])
# print(dp[-1])
w = open('muggers.out', 'w')
w.write(str(dp[-1]))
w.close()