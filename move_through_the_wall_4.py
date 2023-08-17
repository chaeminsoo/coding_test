# 16946
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input()))

visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,n,m):
    passed = []
    q = deque()
    visited[i][j] = True
    q.append([i,j])
    cnt = 1

    while q:
        x,y = q.popleft()
        passed.append([x,y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < n and ny >=0 and ny < m and not visited[nx][ny] and board[nx][ny] == '0':
                q.append([nx,ny])
                cnt+=1
                visited[nx][ny] = True
    
    return cnt, passed

what_block = {}
can_move_num = {}
nnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '0' and not visited[i][j]:
            cnt,passed = bfs(i,j,n,m)

            for pi,pj in passed:
                what_block[(pi,pj)] = nnt
            can_move_num[nnt] = cnt
            nnt+=1


ans = [['0']*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            cnt = 1
            passed_block = set()

            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if ni >= 0 and ni < n and nj >= 0 and nj < m and board[ni][nj] == '0':
                    passed_block.add(what_block[(ni,nj)])

            for k in passed_block:
                cnt += can_move_num[k]
            ans[i][j] = str(cnt%10)

for i in ans:
    print(''.join(i))