# https://school.programmers.co.kr/learn/courses/30/lessons/250134?language=python3
import sys
sys.setrecursionlimit(10**6)

ans = 1e9

def solution(maze):
    global ans
    N = len(maze)
    M = len(maze[0])
    
    r_vi = [[False]*M for _ in range(N)]
    b_vi = [[False]*M for _ in range(N)]
    
    rs = 0
    bs = 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                rs = [i,j]
                r_vi[i][j] = True
            if maze[i][j] == 2:
                bs = [i,j]
                b_vi[i][j] = True
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def dfs(rx,ry,bx,by,r_vi,b_vi,cnt):
        global ans
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            ans = min(ans,cnt)
            return
                
        if maze[rx][ry] == 3:
            nxt_r = [[rx,ry]]
        else:
            nxt_r = []
        
            for i in range(4):
                nrx = rx + dx[i]
                nry = ry + dy[i]

                if nrx < N and nrx >= 0 and nry >= 0 and nry < M and not r_vi[nrx][nry] and maze[nrx][nry] != 5:
                    nxt_r.append([nrx,nry])
                    
        if maze[bx][by] == 4:
            nxt_b = [[bx,by]]
        else:
            nxt_b = []
        
            for i in range(4):
                nbx = bx + dx[i]
                nby = by + dy[i]

                if nbx < N and nbx >= 0 and nby >= 0 and nby < M and not b_vi[nbx][nby] and maze[nbx][nby] != 5:
                    nxt_b.append([nbx,nby])
                    
    
        for r in nxt_r:
            for b in nxt_b:
                if r == [bx,by] and b == [rx,ry]:
                    continue
                if r == b:
                    continue
                                
                r_vi[r[0]][r[1]] = True
                b_vi[b[0]][b[1]] = True
                dfs(r[0],r[1],b[0],b[1],r_vi,b_vi,cnt+1)
                r_vi[r[0]][r[1]] = False
                b_vi[b[0]][b[1]] = False
                
    dfs(rs[0],rs[1],bs[0],bs[1],r_vi,b_vi,0)
    
    if ans == 1e9:
        return 0
    else:
        return ans