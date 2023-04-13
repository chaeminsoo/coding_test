def checking(x,y,n,board):
    block_num = board[x][y]
    if x+1 < n and y+2<n:
        if board[x+1][y] == block_num and board[x+1][y+1] == block_num and board[x+1][y+2] == block_num:
            return block_num, [(x,y+1),(x,y+2)]
    
    if x+2 < n and y-1 >= 0:
        if board[x+1][y] == block_num and board[x+2][y] == block_num and board[x+2][y-1] == block_num:
            return block_num, [(x+1,y-1), (x,y-1)]
        
    if x+2 < n and y+1 < n:
        if board[x+1][y] == block_num and board[x+2][y] == block_num and board[x+2][y+1] == block_num:
            return block_num, [(x+1,y+1), (x,y+1)]
        
    if x+1 < n and y-2 >= 0:
        if board[x+1][y] == block_num and board[x+1][y-1] == block_num and board[x+1][y-2] == block_num:
            return block_num, [(x,y-1),(x,y-2)]
        
    if x+1 < n and y+1 < n and y-1 >= 0:
        if board[x+1][y] == block_num and board[x+1][y+1] == block_num and board[x+1][y-1] == block_num:
            return block_num, [(x,y+1),(x,y-1)]
        
    return -1,[]
        
        
        

def solution(board):
    n = len(board)
    check_board = [[0]*n for _ in range(n)]
    
    can_remove_blocks = set()
    cant_remove_blocks = set()
    should_check_loc = {}
    block_columns = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                if board[i][j] in block_columns:
                    block_columns[board[i][j]].add(j)
                else:
                    block_columns[board[i][j]] = {j}
                    
                b_num, b_location = checking(i,j,n,board)
                if b_num != -1:
                    can_remove_blocks.add(b_num)
                    for b_l in b_location:
                        if b_num in should_check_loc:
                            should_check_loc[b_num].append(b_l)
                        else:
                            should_check_loc[b_num] = [b_l]
    
    dead_column = set()
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0 and board[r][c] not in can_remove_blocks:
                for i in block_columns[board[r][c]]:
                    dead_column.add(c)
            elif board[r][c] != 0 and board[r][c] in can_remove_blocks:
                for x,y in should_check_loc[board[r][c]]:
                    if y in dead_column:
                        cant_remove_blocks.add(board[r][c])
                        for i in block_columns[board[r][c]]:
                            dead_column.add(c)
                    
                
    return len(can_remove_blocks-cant_remove_blocks)