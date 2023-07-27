# 9252
A = input()
B = input()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])

r = len(A)
c = len(B)

ans = ''
while dp[r][c] != 0:
    if dp[r][c] == dp[r-1][c]:
        r -= 1
    elif dp[r][c] == dp[r][c-1]:
        c -= 1
    else:
        ans += A[r-1]
        r -= 1
        c -= 1

print(ans[::-1])