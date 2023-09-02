from collections import deque

def nxt_road_cost(d1,d2):
    if d1 in {0,1} and d2 in {0,1}:
        return 100
    elif d1 in {2,3} and d2 in {2,3}:
        return 100
    else:
        return 600

def solution(board):
    n = len(board)
    cost_board = [[[1e9]*4 for _ in range(n)] for _ in range(n)]
    for i in range(4):
        cost_board[0][0][i] = 0
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        q.append([0,0,i,0])
    
    while q:
        x,y,d,cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            cost = cnt + nxt_road_cost(d,i)
            
            if nx >= 0 and nx < n and ny >=0 and ny < n and board[nx][ny] != 1 and cost < cost_board[nx][ny][i]:
                cost_board[nx][ny][i] = cost                
                q.append([nx,ny,i,cost])
                
    return min(cost_board[n-1][n-1])