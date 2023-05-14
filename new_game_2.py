# 17837
n, k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

piece_board = [[[] for _ in range(n)] for _ in range(n)]
piece = {}
for i in range(k):
    r,c,d = map(int,input().split())
    piece[i] = [r-1,c-1,d-1]
    piece_board[r-1][c-1].append(i)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def d_change(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2

def move_piece(target):
    r,c,d = piece[target]
    idx = piece_board[r][c].index(target)
    moving_piece = piece_board[r][c][idx:]
    piece_board[r][c] = piece_board[r][c][:idx]

    nx = r + dx[d]
    ny = c + dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2: # 파란색
        d = d_change(d)

        nx = r + dx[d]
        ny = c + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2: # 파란색
            piece_board[r][c] += moving_piece
            if len(piece_board[r][c]) >= 4:
                return True
            for i in moving_piece:
                if i == target:
                    piece[i][2] = d
                piece[i][0] = r
                piece[i][1] = c

        elif board[nx][ny] == 0: # 흰색
            piece_board[nx][ny] += moving_piece
            if len(piece_board[nx][ny]) >= 4:
                return True
            for i in moving_piece:
                if i == target:
                    piece[i][2] = d
                piece[i][0] = nx
                piece[i][1] = ny

        else: # 빨간    
            piece_board[nx][ny] += moving_piece[::-1]
            if len(piece_board[nx][ny]) >= 4:
                return True
            for i in moving_piece:
                if i == target:
                    piece[i][2] = d
                piece[i][0] = nx
                piece[i][1] = ny

    elif board[nx][ny] == 0: # 흰색
        piece_board[nx][ny] += moving_piece
        if len(piece_board[nx][ny]) >= 4:
            return True
        for i in moving_piece:
            piece[i][0] = nx
            piece[i][1] = ny
        
    else: # 빨간    
        piece_board[nx][ny] += moving_piece[::-1]
        if len(piece_board[nx][ny]) >= 4:
            return True
        for i in moving_piece:
            piece[i][0] = nx
            piece[i][1] = ny

for ans in range(1,1001):
    for i in range(k):
        flag = move_piece(i)
        if flag:
            break
    if flag:
        break

if flag:
    print(ans)
else:
    print(-1)