# 16986
from itertools import permutations

n, k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

jioo = list(permutations([i for i in range(1,n+1)],n))
kyunghee = list(map(int,input().split()))
minho = list(map(int,input().split()))

def find_op(op1,op2):
    if 0 not in [op1, op2]:
        return 0
    if 1 not in [op1, op2]:
        return 1
    if 2 not in [op1, op2]:
        return 2

ans = 0
for jio in jioo:
    players = [jio, kyunghee, minho]
    win_records = [0,0,0]
    plans = [0,0,0]
    p1 = 0
    p2 = 1
    while k not in win_records:
        if plans[0] >= n or plans[1] >= 20 or plans[2] >= 20:
            break
        
        p1_rsp = players[p1][plans[p1]]
        p2_rsp = players[p2][plans[p2]]
                
        rslt = board[p1_rsp-1][p2_rsp-1]

        if rslt == 2:
            win_records[p1] +=1
            plans[p1]+=1
            plans[p2]+=1
            p2 = find_op(p1,p2)
        elif rslt == 1:
            if p1 < p2:
                win_records[p2] +=1
                plans[p1]+=1
                plans[p2]+=1
                p1 = find_op(p1,p2)
            else:
                win_records[p1] +=1
                plans[p1]+=1
                plans[p2]+=1
                p2 = find_op(p1,p2)
        else:
            win_records[p2] +=1
            plans[p1]+=1
            plans[p2]+=1
            p1 = find_op(p1,p2)

    if win_records[0] >= k:
        ans = 1

print(ans)