def get_next_loc(board, loc):
    n = len(board)
    m = len(board[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    nxt_loc = []
    
    for i in range(4):
        nx = loc[0] + dx[i]
        ny = loc[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
            nxt_loc.append([nx,ny])
    return nxt_loc

def dfs(board, aloc, bloc, step):
    if step%2==0:
        nxt_loc = get_next_loc(board, aloc)
    else:
        nxt_loc = get_next_loc(board, bloc)
        
    if not nxt_loc: # 현재 턴의 player가 이동할 수 없다
        return step%2 != 0, step # 본인이 졌다, 이동 한 횟수
    if aloc == bloc:
        return step%2 == 0, step+1 # 본인이 이겼다, 이동 한 횟수(한턴 더 지나가야하니까)
    
    win, lose = [], []
    if step % 2 == 0: # a차례
        board[aloc[0]][aloc[1]] = 0
        for nr, nc in nxt_loc:
            is_a_win, cnt = dfs(board, [nr,nc], bloc, step+1)
            if is_a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    
    else: # a차례
        board[bloc[0]][bloc[1]] = 0
        for nr, nc in nxt_loc:
            is_a_win, cnt = dfs(board, aloc, [nr,nc], step+1)
            if not is_a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[bloc[0]][bloc[1]] = 1
    
    if win:
        return step%2==0, min(win) # 이긴 경우 젤 짧은 루트
    else:
        return step%2!=0, max(lose) # 진 경우 젤 긴 루트
    
    
def solution(board, aloc, bloc):
    winner, step = dfs(board, aloc, bloc, 0) # a가 이겼는지 졌는지
    return step