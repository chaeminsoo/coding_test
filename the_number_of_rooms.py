# https://school.programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    loc = (0,0)
    Vs = set()
    Es = set()
    Vs.add(loc)
    for a in arrows:
        for _ in range(2):
            nxt_loc = (loc[0]+dx[a], loc[1]+dy[a])
            Vs.add(nxt_loc)
            Es.add((nxt_loc, loc))
            Es.add((loc, nxt_loc))
            loc = nxt_loc
    
    v = len(Vs)
    e = len(Es)//2

    return 1+e-v

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
# 3