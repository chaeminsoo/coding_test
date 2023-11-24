# https://school.programmers.co.kr/learn/courses/30/lessons/250136
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for _ in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        q = deque()
        visited[x][y] = True
        q.append([x,y])
        cnt = 0
        loc = []
        while q:
            x,y = q.popleft()
            cnt+=1
            loc.append([x,y])
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= 0 and nx < n and ny >= 0 and ny < m and land[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx,ny])
        
        return cnt, loc
                    
        
    board = [[0]*m for _ in range(n)]
    block_num = 1
    block_how_many = {}
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                cnt, loc = bfs(i,j)
                for x,y in loc:
                    board[x][y] = block_num
                block_how_many[block_num] = cnt
                block_num+=1
                
                
    ans = 0
    for j in range(m):
        get_blocks = set()
        rslt = 0
        for i in range(n):
            if board[i][j]:
                get_blocks.add(board[i][j])
        for i in get_blocks:
            rslt += block_how_many[i]
        ans = max(ans,rslt)
    
    return ans