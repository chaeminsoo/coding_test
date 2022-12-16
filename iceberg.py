# 2573
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def ice_melt():
    global n,m
    melt_board = [[0]*m for _ in range(n)]
    ice_left = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            if board[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                        cnt+=1
                melt_board[i][j] = max(board[i][j]-cnt,0)
                ice_left += melt_board[i][j]
    if ice_left:
        return melt_board, True
    else:
        return melt_board, False

def BFS():
    global n,m
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        nx = x +dx[k]
                        ny = y +dy[k]

                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 0 and not visited[nx][ny]:
                            q.append([nx,ny])
                            visited[nx][ny] = True
                cnt+=1
    return cnt


ice_left = True
ynt = 0
while ice_left:
    board, ice_left = ice_melt()
    ynt+=1
    if BFS() >= 2:
        break
if ice_left:
    print(ynt)
else:
    print(0)