# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    all_blocks = brown + yellow
    for garo in range(3,all_blocks):
        if all_blocks%garo != 0:
            continue
        else:
            sero = all_blocks//garo
            if sero > garo:
                continue
            
            if (garo-2)*(sero-2) == yellow:
                return [garo,sero]
            
            