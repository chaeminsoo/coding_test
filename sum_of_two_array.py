# 2143
from collections import defaultdict

t = int(input())

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

sums = defaultdict(int)

for i in range(n):
    for j in range(i+1,n+1):
        sums[sum(A[i:j])] += 1

ans = 0
for i in range(m):
    for j in range(i+1,m+1):
        ans += sums[t-sum(B[i:j])]

print(ans)