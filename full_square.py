# https://school.programmers.co.kr/learn/courses/30/lessons/62048
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def solution(w,h):
    total = w*h
    gcd_ = gcd(w,h)
    w = w//gcd_
    h = h//gcd_
    return total - (w+h-1)*gcd_