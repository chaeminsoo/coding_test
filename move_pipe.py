# 17070
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# [i][j][k] : i,j에 k방향으로 도착하는 경우의 수
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(2,n):
        if board[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if board[i-1][j] == 0 and board[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[-1][-1]))