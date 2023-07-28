# 2239
sudoku = []
for _ in range(9):
    sudoku.append(list(map(int,list(input()))))

def row_check(r,n,sudoku):
    for i in range(9):
        if n == sudoku[r][i]:
            return False
    return True

def column_check(c,n,sudoku):
    for i in range(9):
        if n == sudoku[i][c]:
            return False
    return True

def block_check(r,c,n,sudoku):
    for i in range(3):
        for j in range(3):
            if n == sudoku[r//3*3 +i][c//3*3 +j]:
                return False
    return True

def nxt_loc(x,y):
    if y < 8:
        return (x,y+1)
    return (x+1,0)

def dfs(x,y):
    if x >= 9:
        for i in sudoku:
            print(*i)
        exit()
    
    nxt_x, nxt_y = nxt_loc(x,y)

    if sudoku[x][y] != 0:
        dfs(nxt_x, nxt_y)
    else:
        for i in range(1,10):
            if row_check(x,i,sudoku) and column_check(y,i,sudoku) and block_check(x,y,i,sudoku):
                sudoku[x][y] = i
                dfs(nxt_x, nxt_y)
                sudoku[x][y] = 0

dfs(0,0)