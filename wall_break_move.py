# 2206
from collections import deque

n,m = map(int,input().split())

board = []
for _ in range(n):
    board.append(list(map(int,list(input()))))

num_board = [[1e9]*m for _ in range(n)]
break_num_board = [[1e9]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append([0,0,1,0])
ans = 1e9
while q:
    x,y,c,b = q.popleft()
    if x == n-1 and y == m-1:
        ans = min(ans,c)
        continue
        

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if b == 0:
                if num_board[nx][ny] > c+1:
                    if board[nx][ny] == 0:
                        q.append([nx,ny,c+1,b])
                    else:
                        q.append([nx,ny,c+1,b+1])
                    num_board[nx][ny] = c+1
            else:
                if break_num_board[nx][ny] > c+1 and board[nx][ny] == 0:
                    q.append([nx,ny,c+1,b])
                    break_num_board[nx][ny] = c+1

if ans == 1e9:
    print(-1)
else:
    print(ans)