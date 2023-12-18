# https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math

def solution(n, stations, w):
    ans = 0
    before_s = 0
    for i in stations:
        left = i-w
        no_s_num = left-before_s-1
        new_s = math.ceil(no_s_num/(w*2 +1))
        ans += new_s
        before_s = i+w
    
    # stations 끝이랑 n이랑 안 맞는 경우
    if before_s != n:
        no_s_num = (n+1)-before_s-1
        new_s = math.ceil(no_s_num/(w*2 +1))
        ans += new_s
    
    return ans