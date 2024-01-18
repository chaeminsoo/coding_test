# https://school.programmers.co.kr/learn/courses/30/lessons/142085?language=python3
import heapq

def solution(n, k, enemy):
    use_k = []
    damage = 0
    ans = 0
    for i in enemy:
        heapq.heappush(use_k,i)
        if len(use_k) > k:
            d = heapq.heappop(use_k)
            damage+=d
            if damage > n:
                break
        ans+=1
    return ans