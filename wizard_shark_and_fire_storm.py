# 20058
from collections import deque

n,q = map(int,input().split())
N=2**n
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

ls = list(map(int,input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def turn(l,N):
    L = 2**l
    ref_board = [[0]*(N) for _ in range(N)]
    for i in range(0,N,L):
        for j in range(0,N,L):
            for x in range(L):
                for y in range(L):
                    ref_board[y+i][L-x-1+j] = board[x+i][y+j]
    return ref_board

for l in ls:
    board = turn(l,N)
    melt = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            if board[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if nx >= 0 and nx < N and ny >= 0 and ny < N and board[nx][ny] != 0:
                        cnt+=1
                if cnt < 3:
                    melt.append([i,j])
    for i,j in melt:
        board[i][j] = max(board[i][j]-1,0)

visited = [[False]*N for _ in range(N)]

def bfs(x,y):
    global ans_1
    q = deque()
    q.append([x,y])

    cnt = 0
    while q:
        r,c = q.pop()
        ans_1+=board[r][c]
        cnt+=1

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if nx >= 0 and nx < N and ny >=0 and ny < N and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                q.append([nx,ny])
    return cnt

ans_1 = 0
ans_2 = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and not visited[i][j]:
            visited[i][j] = True
            ans_2 = max(bfs(i,j),ans_2)

print(ans_1)
print(ans_2)