# 2342
order = list(map(int,input().split()))
n = len(order)

order = [0] + order[:-1]

dp = [[[1e9]*5 for _ in range(5)] for _ in range(n)]
dp[0][0][0] = 0

def left(n):
    if n == 4: return 1
    return n+1

def right(n):
    if n == 1: return 4
    return n-1

def cross(n):
    if n in {1,2}:
        return n+2
    return n-2

for i in range(1,n):
    desti = order[i]
    for l in range(5):
        for r in range(5):
            if l == r:
                continue

            if l == desti:
                dp[i][l][r] = min(dp[i-1][left(l)][r]+3, dp[i-1][right(l)][r]+3, dp[i-1][cross(l)][r]+4, dp[i-1][l][r]+1, dp[i-1][0][r]+2)
            if r == desti:
                dp[i][l][r] = min(dp[i-1][l][left(r)]+3, dp[i-1][l][right(r)]+3, dp[i-1][l][cross(r)]+4, dp[i-1][l][r]+1, dp[i-1][l][0]+2)

ans = 1e9
for i in dp[n-1]:
    rslt = min(i)
    ans = min(ans,rslt)

print(ans)