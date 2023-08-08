# 2568
from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
wires = []
b_to_a = {}
all_a = set()
for _ in range(n):
    a,b = map(int,input().split())
    wires.append([a-1,b-1])
    b_to_a[b-1] = a-1
    all_a.add(a-1)

wires.sort()

dp = [1e9]*n
dp_2 = [1e9]*n

for i,ab in enumerate(wires):
    idx = bisect_left(dp,ab[1])
    dp[idx] = ab[1]
    dp_2[i] = idx
    
cnt = 0
for i in dp:
    if i == 1e9:
        break
    cnt+=1
print(n-cnt)

cnt -= 1
remains = set()
for i in range(n-1,-1,-1):
    if cnt < 0:
        break
    if dp_2[i] == cnt:
        remains.add(b_to_a[wires[i][1]])
        cnt-=1

ans = list(all_a-remains)
ans.sort()
for i in ans:
    print(i+1)