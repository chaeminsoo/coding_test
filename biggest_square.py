# 1915
n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))

size_board = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def checking(x,y):
    if x > 0 and x < n and y > 0 and y < m:
        l = int(size_board[x+dx[2]][y+dy[2]])
        u = int(size_board[x+dx[0]][y+dy[0]])
        ul = int(size_board[x+dx[0]][y+dy[2]])
        
        return min(l,u,ul)+1

    else:
        return 1
    
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            sq_edge = checking(i,j)
            ans = max(ans,sq_edge)
            size_board[i][j] = sq_edge

print(ans**2)           