from collections import deque

def block_sum(bl):
    cnt = 0
    for b in bl:
        cnt += sum(b)
    return cnt        

def clock_90(l):
    l = list(zip(*l[::-1]))
    return list(map(list,l))

def solution(game_board, table):
    ans = 0
    n = len(table)
    for i in range(n):
        for j in range(n):
            game_board[i][j] = (game_board[i][j]+1)%2
    
    visited = [[False]*n for _ in range(n)]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def bfs(r,c,n, board):
        t_,b_,l_,r_ = r,0,c,0
        q = deque()
        q.append([r,c])
        visited[r][c] = True
        cnt = 0
        while q:
            r,c = q.popleft()
            cnt+=1
            
            t_ = min(r,t_)
            b_ = max(r,b_)
            l_ = min(l_,c)
            r_ = max(r_,c)            
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if nr >= 0 and nr < n and nc >= 0 and nc < n and not visited[nr][nc] and board[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append([nr,nc])
        
        rslt = []
        for i in range(t_,b_+1):
            ref = []
            for j in range(l_, r_+1):
                ref.append(board[i][j])
            rslt.append(ref)
                
        return rslt
                
    blanks = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 1 and not visited[i][j]:
                blanks.append(bfs(i,j,n, game_board))
    visited = [[False]*n for _ in range(n)]
    
    blocks = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                blocks.append(bfs(i,j,n, table))
    
    more_blocks = []
    for bl in blocks:
        ref = []
        for _ in range(4):
            bl = clock_90(bl)
            ref.append(bl)
        more_blocks.append(ref)
    
    blocks = [True]*len(more_blocks)
    
    for bl in blanks:
        for i in range(len(more_blocks)):
            if blocks[i]:
                if bl in more_blocks[i]:
                    ans += block_sum(bl)
                    blocks[i] = False
                    break
                    
    return ans