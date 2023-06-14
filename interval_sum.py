# 2042
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = [0]*(n+1)
tree = [0]*(n+1)

def update(i,num):
    while i <= n:
        tree[i] += num
        i += (i&-i)

def prefix_sum(i):
    rslt = 0
    while i > 0:
        rslt += tree[i]
        i -= (i&-i)
    return rslt

for i in range(n):
    x = int(input())
    nums[i+1] = x
    update(i+1,x)    

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b, c - nums[b])
        nums[b] = c
    else:
        print(prefix_sum(c)-prefix_sum(b-1))