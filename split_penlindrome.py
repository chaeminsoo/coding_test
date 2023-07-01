# 1509
data = input()
n = len(data)

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if data[i] == data[i+1]:
        dp[i][i+1] = 1

for i in range(n):
    for j in range(n):
        if i+j >= n:
            continue

        if j == i+j or j+1 == i+j:
            continue

        if data[j] == data[i+j]:
            if dp[j+1][i+j-1]:
                dp[j][i+j] = 1

ans = [1e9]*(n+1)
ans[-1] = 0
for ed in range(n):
    for st in range(n):
        if dp[st][ed] == 1:
            ans[ed] = min(ans[ed], ans[st-1]+1)
        else:
            ans[ed] = min(ans[ed], ans[ed-1]+1)

print(ans[n-1])