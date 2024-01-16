# https://school.programmers.co.kr/learn/courses/30/lessons/169198
def solution(m, n, startX, startY, balls):
    ans = []
    for x,y in balls:
        rslt = 1e9
        
        for i,j in [[0,(n-y)*2], [0,-2*y], [-2*x,0], [(m-x)*2,0]]:
            nx = x + i
            ny = y + j
            
            if startY == ny and startX > x and startX > nx:
                continue
            if startY == ny and startX < x and startX < nx:
                continue
            if startX == nx and startY > y and startY > ny:
                continue
            if startX == nx and startY < y and startY < ny:
                continue
            
            dist = (nx-startX)**2 + (ny-startY)**2
            rslt = min(rslt,dist)
        
        ans.append(rslt)
    
    return ans