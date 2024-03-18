# https://school.programmers.co.kr/learn/courses/30/lessons/68645#
from collections import deque

def solution(n):
    board = [[0]*n for _ in range(n)]
    dx = [1,0,-1]
    dy = [0,1,-1]
    d = 0
    cnt = 1
    q = deque()
    q.append([0,0])
    while q:
        x,y = q.popleft()
        board[x][y] = cnt
        cnt+=1
        
        for _ in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx >= 0 and nx < n and ny >=0 and ny < n and board[nx][ny] == 0:
                q.append([nx,ny])
                break
            else:
                d = (d+1)%3
    
    ans = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                ans.append(board[i][j])
    
    return ans