# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# from collections import deque

# O(n^2)
# def solution(prices):
#     q = deque(prices)
    
#     ans = []
    
#     while q:
#         cnt = 0
#         now = q.popleft()
        
#         for i in q:
#             cnt+=1
#             if i < now:
#                 break
#         ans.append(cnt)
    
#     return ans

# O(n)
def solution(prices):
    n = len(prices)
    ans = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        ans[j] = n - 1 - j

    return ans
