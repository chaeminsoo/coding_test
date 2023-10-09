# 2023 현대모비스 알고리즘 경진대회 예선 에어컨
def solution(temperature, t1, t2, a, b, onboard):
    temperature+=10
    t1+=10
    t2+=10
    
    # 가로: 온도, 세로: 시간
    dp = [[100001]*51 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    
    ac = 1
    if temperature > t2:
        ac = -1
    
    for i in range(1,len(onboard)):
        for j in range(51):
            if (onboard[i]==1 and t1 <= j <= t2) or onboard[i]==0:
                # 에어컨 키고 유지
                if t1 <= j <= t2:
                    dp[i][j] = min(dp[i][j],dp[i-1][j]+b)                
                # 에어컨 키고 변화
                if 0 <= j-ac <= 50:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-ac]+a)                
                # 에어컨 안 키고 유지
                if temperature == j:
                    dp[i][j] = min(dp[i][j],dp[i-1][j])                
                # 에어컨 안 키고 변화
                if 0 <= j+ac <= 50:
                    dp[i][j] = min(dp[i][j],dp[i-1][j+ac])                
    
    return min(dp[len(onboard)-1])