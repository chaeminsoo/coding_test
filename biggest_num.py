# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key

def com(str1,str2):
    ref1 = int(str1+str2)
    ref2 = int(str2+str1)
    
    if ref1 > ref2:
        return -1 # 먼저 들어온게(str1) 앞으로
    elif ref1 < ref2:
        return 1 # 먼저 들어온게(str1) 뒤으로
    else:
        return 0 # 순서 변경 없음

def solution(numbers):
    answer = ''
    nums = [str(i) for i in numbers]
    nums.sort(key = cmp_to_key(com))
    
    for i in nums:
        answer+=i
    answer = int(answer)
    return str(answer)