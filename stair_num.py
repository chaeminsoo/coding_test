# 1562
n = int(input())

# dp[i][j][k], i:숫자 사용 상태, j:자릿수, k:마지막 수
dp = [[[0]*10 for _ in  range(n+1)] for _ in range(1<<10)]

# 한자리 수
for i in range(1,10):
    dp[1<<i][1][i] = 1

# 자릿수
for i in range(2,n+1):
    # 마지막 수
    for j in range(10):
        # 숫자 조합
        for k in range(1<<10):
            if j == 0:
                dp[1<<j|k][i][j] += dp[k][i-1][1]
            elif j == 9:
                dp[1<<j|k][i][j] += dp[k][i-1][8]
            else:
                dp[1<<j|k][i][j] += dp[k][i-1][j-1]
                dp[1<<j|k][i][j] += dp[k][i-1][j+1]

ans = 0
for i in range(10):
    ans += dp[(1<<10)-1][n][i]

print(ans%1000000000)