# 11054
from bisect import bisect_left

n = int(input())
array = list(map(int,input().split()))
neg_array = [-i for i in array]

dp = [0]*n
for st in range(n):
    pos_dp = [1e9]*n
    neg_dp = [1e9]*n

    for j in range(st+1):
        idx_pos = bisect_left(pos_dp, array[j])
        pos_dp[idx_pos] = array[j]

    flag = False
    for j in range(st,n):
        idx_neg = bisect_left(neg_dp, neg_array[j])
        if flag and idx_neg == 0:
            continue
        neg_dp[idx_neg] = neg_array[j]
        flag = True
    
    for i in pos_dp:
        if i == 1e9:
            break
        dp[st] += 1

    for i in neg_dp:
        if i == 1e9:
            break
        dp[st] += 1

print(max(dp)-1)