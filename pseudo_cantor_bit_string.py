# https://school.programmers.co.kr/learn/courses/30/lessons/148652?language=python3#
def is_one(i):
    while i > 0:
        i,mod = divmod(i,5)
        if mod == 2:
            return False
    return True

def solution(n, l, r):
    ans = 0
    for i in range(l-1,r):
        if is_one(i):
            ans+=1
    return ans