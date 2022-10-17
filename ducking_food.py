# 1743
from collections import deque

n, m, k = map(int,input().split())

board = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 2

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            q.append((i,j))
            visited[i][j] = True
            board[i][j] = cnt
            while q:
                x,y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                        q.append((nx,ny))
                        board[nx][ny] = cnt
                        visited[nx][ny] = True
            cnt+=1

food_size = [0]*(10001)
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            food_size[board[i][j]] += 1
print(max(food_size))