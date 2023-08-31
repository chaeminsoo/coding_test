# 2023 KAKAO BLIND RECRUITMENT 미로 탈출 명령어
# d l r u
import heapq

def can_go(x,y,r,c,left_dist):
    ref = abs(x-r)+abs(y-c)
    if left_dist < ref:
        return False
    if (left_dist-ref)%2 != 0:
        return False
    return True

def solution(n, m, x, y, r, c, k):
    x-=1; y-=1; r-=1; c-=1
    path = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    d = ['u','d','l','r']
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            heapq.heappush(path, [d[i], 1, [nx,ny]])

    while path:
        passed, cnt, now_loc = heapq.heappop(path)
        if now_loc[0] == r and now_loc[1] == c and cnt == k:
            return passed
        
        if not can_go(now_loc[0],now_loc[1],r,c,k-cnt):
            continue

        for i in range(4):
            nx = now_loc[0] + dx[i]
            ny = now_loc[1] + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                heapq.heappush(path, [passed+d[i], cnt+1, [nx,ny]])

    return "impossible"