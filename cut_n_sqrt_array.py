# https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    ans = []
    for i in range(left,right+1):
        ans.append(max(i//n,i%n)+1)
    return ans
        