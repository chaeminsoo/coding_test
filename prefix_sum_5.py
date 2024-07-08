# 11660
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
orders = []

for _ in range(n):
    board.append(list(map(int,input().split())))

dp = [i[:] for i in board]

for r in range(n):
    for c in range(n):
        if c:
            dp[r][c] += dp[r][c-1]
        else:
            continue

for c in range(n):
    for r in range(n):
        if r:
            dp[r][c] += dp[r-1][c]
        else:
            continue

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    rslt = dp[x2-1][y2-1]
    if y1 != 1:
        rslt -= dp[x2-1][y1-2]
    if x1 != 1:
        rslt -= dp[x1-2][y2-1]
    if x1 != 1 and y1 != 1:
        rslt += dp[x1-2][y1-2]

    print(rslt)