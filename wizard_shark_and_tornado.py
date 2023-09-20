# 20057
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

x = n//2
y = n//2

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0

left_p = [
    [0,0,0.02,0,0],
    [0,0.1,0.07,0.01,0],
    [0.05,0,0,0,0],
    [0,0.1,0.07,0.01,0],
    [0,0,0.02,0,0]
]
up_p = [
    [0,0,0.05,0,0],
    [0,0.1,0,0.1,0],
    [0.02,0.07,0,0.07,0.02],
    [0,0.01,0,0.01,0],
    [0,0,0,0,0]
]
down_p = [
    [0,0,0,0,0],
    [0,0.01,0,0.01,0],
    [0.02,0.07,0,0.07,0.02],
    [0,0.1,0,0.1,0],
    [0,0,0.05,0,0]    
]
right_p = [
    [0,0,0.02,0,0],
    [0,0.01,0.07,0.1,0],
    [0,0,0,0,0.05],
    [0,0.01,0.07,0.1,0],
    [0,0,0.02,0,0]
]

def wind(x,y,d,n):
    if d == 0:
        rslt = 0
        remains = board[x][y]
        for i in range(-2,3):
            ref_i = i+2
            for j in range(-2,3):
                ref_j = j+2
                if left_p[ref_i][ref_j] != 0:
                    ref = int(board[x][y]*left_p[ref_i][ref_j])
                    if x+i >=0 and x+i < n and y+j >= 0 and y+j < n:
                        board[x+i][y+j] += ref
                    else:
                        rslt+=ref
                    remains -= ref
        board[x][y] = 0
        if x >=0 and x < n and y-1 >=0 and y-1<n:
            board[x][y-1] += remains
        else:
            rslt += remains
        return rslt
    if d == 1:
        rslt = 0
        remains = board[x][y]
        for i in range(-2,3):
            ref_i = i+2
            for j in range(-2,3):
                ref_j = j+2
                if down_p[ref_i][ref_j] != 0:
                    ref = int(board[x][y]*down_p[ref_i][ref_j])
                    if x+i >=0 and x+i < n and y+j >= 0 and y+j < n:
                        board[x+i][y+j] += ref
                    else:
                        rslt+=ref
                    remains -= ref
        board[x][y] = 0
        if x+1 >=0 and x+1 < n and y >=0 and y<n:
            board[x+1][y] += remains
        else:
            rslt += remains
        return rslt
    if d == 2:
        rslt = 0
        remains = board[x][y]
        for i in range(-2,3):
            ref_i = i+2
            for j in range(-2,3):
                ref_j = j+2
                if right_p[ref_i][ref_j] != 0:
                    ref = int(board[x][y]*right_p[ref_i][ref_j])
                    if x+i >=0 and x+i < n and y+j >= 0 and y+j < n:
                        board[x+i][y+j] += ref
                    else:
                        rslt+=ref
                    remains -= ref
        board[x][y] = 0
        if x >=0 and x < n and y+1 >=0 and y+1<n:
            board[x][y+1] += remains
        else:
            rslt += remains
        return rslt
    if d == 3:
        rslt = 0
        remains = board[x][y]
        for i in range(-2,3):
            ref_i = i+2
            for j in range(-2,3):
                ref_j = j+2
                if up_p[ref_i][ref_j] != 0:
                    ref = int(board[x][y]*up_p[ref_i][ref_j])
                    if x+i >=0 and x+i < n and y+j >= 0 and y+j < n:
                        board[x+i][y+j] += ref
                    else:
                        rslt+=ref
                    remains -= ref
        board[x][y] = 0
        if x-1 >=0 and x-1 < n and y >=0 and y<n:
            board[x-1][y] += remains
        else:
            rslt += remains
        return rslt
    
d = 0
flag = False
for i in range(1,n+2):
    for _ in range(2):
        for _ in range(i):
            if x == 0 and y == 0:
                flag = True
                break
            x += dx[d]
            y += dy[d]
            rslt = wind(x,y,d,n)
            ans+=rslt

        d = (d+1)%4
        if flag:
            break
    if flag:
        break
    
print(ans)