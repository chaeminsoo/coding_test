# 16724
from collections import deque

n,m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
d = {'U':0,'D':1,'L':2,'R':3}

board = []
for _ in range(n):
    board.append(list(input()))

check_board = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

parent = {}

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def search(x,y,cnt):
    q = deque()
    visited[x][y] = True
    q.append([x,y])
    check_board[x][y] = cnt

    while q:
        r,c = q.popleft()

        nx = r + dx[d[board[r][c]]]
        ny = c + dy[d[board[r][c]]]

        if not visited[nx][ny]:
            check_board[nx][ny] = cnt
            visited[nx][ny] = True
            q.append([nx,ny])
        else:
            if check_board[nx][ny] == cnt:
                parent[cnt] = cnt
            else:
                parent[cnt] = check_board[nx][ny]

cnt = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            search(i,j,cnt)
            cnt+=1

real_parent = set()
for i in parent:
    real_parent.add(find_parent(parent,i))

print(len(real_parent))