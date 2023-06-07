# 2638
from collections import deque

n,m = map(int,input().split())
board = []
cheese = []
for i in range(n):
    data = list(map(int,input().split()))
    board.append(data)
    for j in range(m):
        if data[j] == 1:
            cheese.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def air(x,y):
    q = deque()
    q.append([x,y])
    board[x][y] = 3

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] == 0:
                board[nx][ny] = 3
                q.append([nx,ny])

def check_cheese(cheese):
    left_cheese = []
    removed_cheese = []
    cheese_cnt = 0
    while cheese:
        x,y = cheese.pop()
        cnt = 0
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if board[nx][ny] == 3:
                cnt+=1

        if cnt >= 2:
            removed_cheese.append([x,y])
        else:
            left_cheese.append([x,y])
            cheese_cnt+=1
    
    return cheese_cnt, left_cheese, removed_cheese

air(0,0)
ans = 0
while True:
    cheese_cnt, left_cheese, removed_cheese = check_cheese(cheese)
    ans += 1
    if cheese_cnt == 0:
        break

    cheese = left_cheese
    
    for i,j in removed_cheese:
        air(i,j)

print(ans)