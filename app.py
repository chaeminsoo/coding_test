# 7579
n,m = map(int,input().split())
Ms = list(map(int,input().split()))
Cs = list(map(int,input().split()))

total_cost = sum(Cs)

dp = [[0]*(total_cost+1) for _ in range(n)]

ans = 1e9
for app_idx in range(n):
    for cost_capacity in range(total_cost+1):

        memory, reboot_cost = Ms[app_idx], Cs[app_idx]

        if reboot_cost > cost_capacity:
            dp[app_idx][cost_capacity] = dp[app_idx-1][cost_capacity]
        else:
            dp[app_idx][cost_capacity] = max(dp[app_idx-1][cost_capacity-reboot_cost] + memory, dp[app_idx-1][cost_capacity])

        if dp[app_idx][cost_capacity] >= m and app_idx == n-1:
            ans = min(ans,cost_capacity)

print(ans)