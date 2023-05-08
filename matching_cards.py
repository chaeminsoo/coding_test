from collections import deque
from itertools import permutations

def find_card(board,target,cursor_):
    range_board = [[-1]*4 for _ in range(4)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque()
    q.append([cursor_,0])
    range_board[cursor_[0]][cursor_[1]] = 0
    
    while q:
        a,cost = q.popleft()
        x,y = a
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if  0 <= nx < 4 and 0 <= ny < 4 and range_board[nx][ny] == -1:
                range_board[nx][ny] = cost+1
                q.append([[nx,ny], cost+1])
            
            flag = 0
            while 0 <= nx < 4 and 0 <= ny < 4:
                if board[nx][ny] != 0:
                    flag = 1
                    if range_board[nx][ny] == -1:
                        range_board[nx][ny] = cost+1
                        q.append([[nx,ny], cost+1])
                    break

                nx += dx[i]
                ny += dy[i]
            
            if flag:
                continue
            else:
                nx -= dx[i]
                ny -= dy[i]
                if range_board[nx][ny] == -1:
                    range_board[nx][ny] = cost+1
                    q.append([[nx,ny], cost+1])
                
    
    target_loc = [100,0,0]
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                if range_board[i][j] <= target_loc[0]:
                    target_loc = [range_board[i][j], i, j]

    return target_loc

def solution(board, r, c):
    cards = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.add(board[i][j])
    
    all_cases = list(permutations(cards,len(cards)))
    ans = 1e9
    for case in all_cases:
        ref_board = [i[:] for i in board]
        cnt = 0
        cursor_ = [r,c]
        for c_ in case:
            for _ in range(2):
                rslt = find_card(ref_board,c_,cursor_)
                cnt += rslt[0]
                ref_board[rslt[1]][rslt[2]] = 0
                cursor_ = [rslt[1],rslt[2]]
        ans = min(ans,cnt+2*len(cards))
        
    return ans