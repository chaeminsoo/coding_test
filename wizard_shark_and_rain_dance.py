# 21610
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
orders = []
for _ in range(m):
    orders.append(list(map(int,input().split())))

cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

for d,s in orders:
    was_c = set()
    while cloud:
        x,y = cloud.pop()
        nx = (x + s*dx[d])%n
        ny = (y + s*dy[d])%n
        was_c.add((nx,ny))
        board[nx][ny]+=1
    for x,y in was_c:
        for d in [2,4,6,8]:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx < n and ny >=0 and ny < n and board[nx][ny] > 0:
                board[x][y] += 1
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i,j) not in was_c:
                cloud.append([i,j])
                board[i][j] -= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += board[i][j]
print(ans)