# 11049
n = int(input())
matrix = []
for _ in range(n):
    a,b = map(int,input().split())
    matrix.append((a,b))

dp = [[1e9]*n for _ in range(n)]

for i in range(n-1):
    dp[i][i] = 0
    dp[i+1][i+1] = 0
    dp[i][i+1] = matrix[i][0]*matrix[i][1]*matrix[i+1][1]

for j in range(2,n):
    for i in range(n-j):
        tmp = 1e9
        for k in range(i,i+j):
            tmp = min(dp[i][k] + dp[k+1][i+j] + (matrix[i][0]*matrix[k][1]*matrix[i+j][1]), tmp)
        dp[i][i+j] = tmp

print(dp[0][-1])