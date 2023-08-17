# 14939
board = []
for _ in range(10):
    board.append(list(input()))

def sw(board,i,j):
    if board[i][j] == '#':
        board[i][j] = 'O'
    else:
        board[i][j] = '#'
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]

        if nx >= 0 and nx < 10 and ny >= 0 and ny < 10:
            if board[nx][ny] == '#':
                board[nx][ny] = 'O'
            else:
                board[nx][ny] = '#'
    
    return board

first_lines_board = []
first_lines_board_how_many = []


def make_first_line(b,column,cnt):
    if column == 10:
        first_lines_board.append(b)
        first_lines_board_how_many.append(cnt)
        return
    
    ref_b = [i[:] for i in b]
    make_first_line(sw(ref_b,0,column),column+1,cnt+1)
    make_first_line(b,column+1,cnt)

make_first_line(board,0,0)

def check(board):
    cnt = 0

    for i in range(1,10):
        for j in range(10):
            if board[i-1][j] == 'O':
                board = sw(board,i,j)
                cnt+=1

    all_off = True
    for i in range(10):
        if board[9][i] == "O":
            all_off = False
            break
    
    if all_off:
        return cnt
    else:
        return 1e9

ans = 1e9
for i in range(1024):
    b = first_lines_board[i]
    cnt = check(b)
    ans = min(ans,cnt+first_lines_board_how_many[i])

if ans == 1e9:
    print(-1)
else:
    print(ans)