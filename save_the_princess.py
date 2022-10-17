# 17836
from collections import deque

n,m,t = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

visited = [[False]*m for _ in range(n)]
costs = [[0]*m for _ in range(n)]
costs[n-1][m-1] = 1e9

q = deque()
q.append((0,0,0))
visited[0][0] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]
gram = 0
while q:
    x,y,c = q.popleft()
    costs[x][y] = c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1 and not visited[nx][ny]:
            if board[nx][ny] == 2:
                gram = [nx,ny]
            visited[nx][ny] = True
            q.append((nx,ny,c+1))

nt = costs[n-1][m-1]
if gram == 0:
    gt = 1e9
else:
    gt = costs[gram[0]][gram[1]] + abs(gram[0] - (n-1)) + abs(gram[1] - (m-1))
if min(gt,nt) > t:
    print('Fail')
else:
    print(min(nt,gt))