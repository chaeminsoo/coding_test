# https://school.programmers.co.kr/learn/courses/30/lessons/136797?language=python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

cost = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3], # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], # 9
]

def solution(numbers):
    # dp[i][(l,r)] : 숫자 i를 누른 상태에서 왼손이 l, 오른손이 r에 있는 경우의 최솟값
    dp = defaultdict(dict)
    numbers = [int(i) for i in numbers]
    
    # 왼손이 l, 오른손이 r에 있을때, num[idx]를 누르기 위한 최소 비용
    def dfs(idx,l,r,num):
        if idx == len(num):
            return 0
        
        if (l,r) in dp[idx]:
            return dp[idx][(l,r)]
        
        c = 1e10
        target = num[idx]
        # 왼손을 이동하는 경우
        if target != r:
            c = min(c, dfs(idx+1,target,r,num) + cost[l][target])
        # 오른손을 이동하는 경우
        if target != l:
            c = min(c, dfs(idx+1,l,target,num) + cost[r][target])
        
        dp[idx][(l,r)] = c
        return c
            
    return dfs(0,4,6,numbers)