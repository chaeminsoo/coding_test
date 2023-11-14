# https://school.programmers.co.kr/learn/courses/30/lessons/131129?language=python3
def solution(target):
    dp = [[1e9,0] for _ in range(max(64,target+1))]
    dp[0] = [0,0]
    dp[50] = [1,1]
    for i in range(1,21):
        dp[i] = [1,1]
        dp[i*2] = [1,0]
        dp[i*3] = [1,0]
        
    sing = [i for i in range(1,21)]
    dub = [i*2 for i in range(1,21)]
    trip = [i*3 for i in range(1,21)]
    bull = [50]
    
    for nums in [sing,dub,trip,bull]:
        if nums == sing or nums == bull:
            flag = True
        else:
            flag = False
            
        for n in nums:
            for i in range(n,target+1):
                if dp[i][0] > dp[i-n][0]+1:
                    dp[i][0] = dp[i-n][0]+1
                    if flag:
                        dp[i][1] = dp[i-n][1]+1
                    else:
                        dp[i][1] = dp[i-n][1]
                elif dp[i][0] == dp[i-n][0]+1:
                    if flag and dp[i][1] < dp[i-n][1]+1:
                        dp[i][1] = dp[i-n][1]+1
                        

    return dp[target]