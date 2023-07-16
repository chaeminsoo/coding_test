# 2098
N = int(input())
roads = []
for _ in range(N):
    roads.append(list(map(int,input().split())))

dp = [[0]*(1<<N-1) for _ in range(N)]

def solution(i,route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1<<(N-1)) -1:
        if roads[i][0]: # 0에서 출발할 거니까, 0으로 돌아오는 값
            return roads[i][0]
        else:
            return 1e9
        
    minimum_dist = 1e9
    for j in range(1,N):
        if not roads[i][j]:
            continue
        if route & (1<<j-1):
            continue
        dist = roads[i][j] + solution(j,route|(1<<j-1))
        minimum_dist = min(minimum_dist, dist)
    dp[i][route] = minimum_dist

    return minimum_dist

print(solution(0,0))
