# 2169
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

q = deque()
num_board = [[0]*m for _ in range(n)]

for i in range(m):
    num_board[0][i] = num_board[0][i-1] + board[0][i]

dy = [-1,1]

for i in range(1,n):
    from_left = [0]*m
    from_right = [0]*m
    for j in range(m):
        if j == 0:
            from_left[j] = board[i][j] + num_board[i-1][j]
        else:
            from_left[j] = max(board[i][j] + num_board[i-1][j], board[i][j] + from_left[j-1])

    for j in range(m-1,-1,-1):
        if j == m-1:
            from_right[j] = board[i][j] + num_board[i-1][j]
        else:
            from_right[j] = max(board[i][j] + num_board[i-1][j], board[i][j] + from_right[j+1])
    
    for j in range(m):
        num_board[i][j] = max(from_left[j], from_right[j])

print(num_board[-1][-1])