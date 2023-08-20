# 20303
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
candy = list(map(int,input().split()))

parent = [i for i in range(n)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

candy_group = [[0,0] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a-1,b-1)

for i in range(n):
    parent[i] = find_parent(parent,parent[i])

candy_group = {}
for i in range(n):
    if parent[i] in candy_group:
        candy_group[parent[i]][0] += 1
        candy_group[parent[i]][1] += candy[i]
    else:
        candy_group[parent[i]] = [1,candy[i]]

candy_group_val = list(candy_group.values())

dp = [[0]*(k) for _ in range(len(candy_group_val))]

ans = 0
for candy_idx in range(len(candy_group_val)):
    for cost_capacity in range(k):

        gain_candy, cost = candy_group_val[candy_idx][1], candy_group_val[candy_idx][0]

        if cost > cost_capacity:
            dp[candy_idx][cost_capacity] = dp[candy_idx-1][cost_capacity]
        else:
            dp[candy_idx][cost_capacity] = max(dp[candy_idx-1][cost_capacity-cost]+gain_candy,dp[candy_idx-1][cost_capacity])

print(dp[-1][-1])