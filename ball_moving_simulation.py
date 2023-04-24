# https://school.programmers.co.kr/learn/courses/30/lessons/87391#
def solution(n, m, x, y, queries):
    t_,b_,l_,r_ = x,x,y,y
    while queries:
        d, a = queries.pop()
        
        if d == 0:
            r_ += a
            if r_ > m-1:
                r_ = m-1
            if l_ != 0:
                l_ += a
    
        elif d == 1:
            l_ -= a
            if l_ < 0:
                l_ = 0
            if r_ != m-1:
                r_ -= a
                
        elif d == 2:
            b_ += a
            if b_ > n-1:
                b_ = n-1
            if t_ != 0:
                t_ += a
                
        elif d == 3:
            t_ -= a
            if t_ < 0:
                t_ = 0
            if b_ != n-1:
                b_ -= a
        
        if r_ < 0 or r_ >= m or l_ < 0 or l_ >= m or t_ < 0 or t_ >= n or b_ < 0 or b_ >= n:
            return 0
            
    return (b_-t_+1)*(r_-l_+1)