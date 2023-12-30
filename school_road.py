# https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]
    p_set = set()
    for i,j in puddles:
        p_set.add((j-1,i-1))
    
    for i in range(m):
        if (0,i) in p_set:
            break
        board[0][i] = 1
    
    for i in range(n):
        if (i,0) in p_set:
            break
        board[i][0] = 1
    
    for i in range(1,n):
        for j in range(1,m):
            if (i,j) in p_set:
                continue
            
            board[i][j] = (board[i-1][j]+board[i][j-1])%1000000007
    
    return board[-1][-1]