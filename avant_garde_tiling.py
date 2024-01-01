# https://school.programmers.co.kr/learn/courses/30/lessons/181186

# 여기 참고: https://ampersandor.tistory.com/21
# 각 단계에서 새롭게 등장하는 타일의 개수를 찾아라! (회전은 할 수 없다고 가정)
# n = 1인 경우, 1개가 새로 등장
# n = 2인 경우, 2개가 새로 등장
# n = 3인 경우, 5개가 새로 등장
# n = 4인 경우, 2개가 새로 등장
# n = 5인 경우, 2개가 새로 등장
# n = 6인 경우, 4개가 새로 등장
# n = 7 이상인 경우는, 4,5,6에서 3씩 늘려주는 경우 밖에 없다
# 점화식이 4이후로 반복된다.
# 식 2개를 만들어서 빼주면 반복되는 부분을 제거할 수 있다.
# 점화식 : dp[i] = dp[i-1] + dp[i-2]*2 + dp[i-3]*5 + dp[i-4]*2 + dp[i-5]*2 + dp[i-6]*4 + dp[i-7]*2 + dp[i-8]*2 + dp[i-9]*4 + ... + dp[0]*(2,2,4 중 하나)

def solution(n):
    dp = [1,1,3,10,23,62]
    if n < 6:
        return dp[n]
    
    for i in range(6,n+1):
        rslt = (dp[-1] + dp[-2]*2 + dp[-3]*6 + dp[-4] - dp[-6])%1000000007
        dp.append(rslt)
    
    return dp[-1]
    