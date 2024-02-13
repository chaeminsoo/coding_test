# 4485
from collections import deque

cnt = 0
while True:
    cnt+=1
    n = int(input())
    if n == 0:
        break

    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    num_board = [[1e9]*n for _ in range(n)]
    num_board[0][0] = board[0][0]
    q = deque()
    q.append([0,0])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                score = num_board[x][y] + board[nx][ny]
                if score < num_board[nx][ny]:
                    num_board[nx][ny] = score
                    q.append([nx,ny])
    
    print(f'Problem {cnt}:',num_board[n-1][n-1])