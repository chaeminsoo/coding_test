# 1106
c, n = map(int,input().split())
data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append([a,b])

dp = [1e9]*2000
dp[0] = 0

for d, ppl in data:
    for i in range(ppl,c+100):
        dp[i] = min(dp[i-ppl]+d,dp[i])
print(min(dp[c:]))