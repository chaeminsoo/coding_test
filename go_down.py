# 2096
import sys
input = sys.stdin.readline

n = int(input())
max_v = [0,0,0]
min_v = [0,0,0]
for i in range(n):
    a,b,c = map(int,input().split())
    if i == 0:
        max_v = [a,b,c]
        min_v = [a,b,c]
        continue
    
    tmp1 = a + max(max_v[0], max_v[1])
    tmp2 = b + max(max_v[0], max_v[1], max_v[2])
    tmp3 = c + max(max_v[1], max_v[2])
    max_v[0] = tmp1
    max_v[1] = tmp2
    max_v[2] = tmp3

    tmp1 = a + min(min_v[0], min_v[1])
    tmp2 = b + min(min_v[0], min_v[1], min_v[2])
    tmp3 = c + min(min_v[1], min_v[2])
    min_v[0] = tmp1
    min_v[1] = tmp2
    min_v[2] = tmp3
    
print(max(max_v),end=' ')
print(min(min_v))