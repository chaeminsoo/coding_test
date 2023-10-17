# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'G':
                goal = [i,j]
            if board[i][j] == 'R':
                st = [i,j]
    
    ans = 1e9
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append([st[0],st[1],0])
    while q:
        x,y,c = q.popleft()
        if [x,y] == goal:
            ans = min(ans,c)
            break
            
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                    
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,c+1])
    
    if ans == 1e9:
        return -1
    else:
        return ans