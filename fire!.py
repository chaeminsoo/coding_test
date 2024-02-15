# 4179
from collections import deque

r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(list(input()))

fire = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            player = [i,j,0]
        if board[i][j] == 'F':
            fire.append([i,j,0])

fire_board = [[1e9]*c for _ in range(r)]
player_board = [[1e9]*c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*c for _ in range(r)]
while fire:
    x,y,cnt = fire.popleft()
    fire_board[x][y] = cnt
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < r and ny >= 0 and ny < c and board[nx][ny] != '#' and not visited[nx][ny]:
            visited[nx][ny] = True
            fire.append([nx,ny,cnt+1])


ans = 1e9
q = deque()
q.append(player)
visited = [[False]*c for _ in range(r)]
visited[player[0]][player[1]] = True
while q:
    x,y,cnt = q.popleft()
    player_board[x][y] = cnt
    if (x == 0 or x == r-1 or y == 0 or y == c-1) and cnt < fire_board[x][y]:
        ans = min(ans,cnt+1)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < r and ny >= 0 and ny < c and board[nx][ny] != '#' and not visited[nx][ny] and cnt+1 < fire_board[nx][ny]:
            visited[nx][ny] = True

            q.append([nx,ny,cnt+1])

if ans == 1e9:
    print('IMPOSSIBLE')
else:
    print(ans)