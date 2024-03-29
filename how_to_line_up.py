# https://school.programmers.co.kr/learn/courses/30/lessons/12936
import math

def solution(n, k):
    ans = []
    nums = [i for i in range(1,n+1)]
    
    while n:
        cases = math.factorial(n-1)
        idx = k // cases
        k %= cases
        if k == 0:
            ans.append(nums.pop(idx-1))
        else:
            ans.append(nums.pop(idx))
        n-=1
    
    return ans
        