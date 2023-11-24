# https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker[0],sticker[1])
    else:
        # 첫번째꺼 뜯는 경우
        dp = [0]*n
        dp[0] = sticker[0]
        dp[1] = max(sticker[0],sticker[1])
        for i in range(2,n-1):
            dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
        
        # 두번째꺼 뜯는 경우
        dp_2 = [0]*n
        dp_2[0] = 0
        dp_2[1] = sticker[1]
        for i in range(2,n):
            dp_2[i] = max(dp_2[i-1], dp_2[i-2]+sticker[i])
            
        return max(max(dp),max(dp_2))