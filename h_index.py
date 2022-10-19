# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)+1):
        if i<= len(citations[bisect_left(citations, i):]):
            answer = max(answer, i)
        
    return answer