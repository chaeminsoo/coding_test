def rotate_90(l):
    ref = zip(*l[::-1])
    return [list(i) for i in ref]

def solution(m, n, board):
    # NxM
    board = rotate_90(board)
    def remove_block(n,m):
        r_block = set()
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != 0:
                    r_block.add((i,j))
                    r_block.add((i+1,j))
                    r_block.add((i,j+1))
                    r_block.add((i+1,j+1))
        if r_block:
            return True, r_block
        else:
            return False, r_block
    
    while True:
        flag,r_block = remove_block(n,m)
        if flag:
            for i,j in r_block:
                board[i][j] = 0
            new_board = []
            for i in range(n):
                ref = []
                cnt = 0
                for j in range(m):
                    if board[i][j] != 0:
                        ref.append(board[i][j])
                        cnt+=1
                ref += [0]*(m-cnt)
                new_board.append(ref)
            board = new_board
        else:
            break
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                ans += 1
    
    return ans