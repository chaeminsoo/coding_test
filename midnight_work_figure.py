# https://school.programmers.co.kr/learn/courses/30/lessons/12927?language=python3
import heapq

def solution(n, works):
    q = []
    for i in works:
        heapq.heappush(q,[-i,i])
    
    while n:
        _,i = heapq.heappop(q)
        i-=1
        n-=1
        heapq.heappush(q,[-i,i])
        
    ans = 0
    for _,i in q:
        if i>0:
            ans += i**2
    return ans