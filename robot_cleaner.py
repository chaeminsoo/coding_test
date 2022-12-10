# 14503
n,m = map(int,input().split())
robot = list(map(int,input().split()))
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

cleaned = [[False]*m for _ in range(n)]

def is_left_dirty(robot):
    r,c,d = robot
    if d == 0:
        if not cleaned[r][c-1] and board[r][c-1] != 1: return True
        else: return False
    if d == 1:
        if not cleaned[r-1][c] and board[r-1][c] != 1: return True
        else: return False
    if d == 2:
        if not cleaned[r][c+1] and board[r][c+1] != 1: return True
        else: return False
    if d == 3:
        if not cleaned[r+1][c] and board[r+1][c] != 1: return True
        else: return False

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 0
turn_cnt = 0
while True:
    x,y,d = robot
    if turn_cnt >= 4:
        op_d = (d+2)%4
        op_x = x + dx[op_d]
        op_y = y + dy[op_d]
        if board[op_x][op_y] == 1:
            break
        else:
            robot = [op_x, op_y, d]
            turn_cnt = 0
            continue

    if not cleaned[x][y]:
        ans += 1
        cleaned[x][y] = True

    if is_left_dirty(robot):
        turn_cnt = 0
        nd = (d+3)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        robot = [nx,ny,nd]
    else:
        nd = (d+3)%4
        robot = [x,y,nd]
        turn_cnt += 1

print(ans)