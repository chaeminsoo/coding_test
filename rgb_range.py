# 1149
import math

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))

dp = [[0,0,0] for _ in range(n)]

for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1,n):
    for j in range(3):
        ref = math.inf
        for k in range(3):
            if j == k:
                continue

            ref = min(ref, dp[i-1][k])

        dp[i][j] = cost[i][j] + ref

print(min(dp[-1]))