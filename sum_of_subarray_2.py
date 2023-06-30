# 1208
from collections import defaultdict

n,s = map(int,input().split())
array = list(map(int,input().split()))

sums = defaultdict(int)

left = array[:n//2]
right = array[n//2:]

def all_sum_right(idx,now_v,arr,n):
    if idx == n:
        sums[now_v] += 1
        return
    all_sum_right(idx+1,now_v+arr[idx],arr,n)
    all_sum_right(idx+1,now_v,arr,n)

ans = 0
def all_sum_left(idx,now_v,arr,n,s):
    global ans
    if idx == n:
        ans += sums[s-now_v]
        return
    all_sum_left(idx+1,now_v+arr[idx],arr,n,s)
    all_sum_left(idx+1,now_v,arr,n,s)

all_sum_right(0,0,right,len(right))
all_sum_left(0,0,left,len(left),s)

if s == 0:
    print(ans-1)
else:
    print(ans)