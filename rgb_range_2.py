# 17404
n = int(input())
paint_cost = []
for _ in range(n):
    paint_cost.append(list(map(int,input().split())))

# dp[i][j] : i번째 집이 j색일때 최소 비용
r_dp = [[1e9]*3 for _ in range(n)]
r_dp[0][0] = paint_cost[0][0]
g_dp = [[1e9]*3 for _ in range(n)]
g_dp[0][1] = paint_cost[0][1]
b_dp = [[1e9]*3 for _ in range(n)]
b_dp[0][2] = paint_cost[0][2]

ans = 1e9
for rgb, dp in enumerate([r_dp,g_dp,b_dp]):
    dp[0][rgb] = paint_cost[0][rgb]
    for i in range(1,n):
        dp[i][0] = paint_cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = paint_cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = paint_cost[i][2] + min(dp[i-1][0], dp[i-1][1])

        if i == n-1:
            if rgb == 0:
                ans = min(dp[i][1],dp[i][2],ans)
            elif rgb == 1:
                ans = min(dp[i][0],dp[i][2],ans)
            else:
                ans = min(dp[i][0],dp[i][1],ans)

print(ans)