# 1388
n, m = map(int,input().split())
board = []
for _ in range(n):
    board.append(input())

def c_turn(l):
    a = zip(*l[::-1])
    return [list(b) for b in a]

ans = 0
for i in range(n):
    ref = ''
    for j in range(m):
        if board[i][j] == '-':
            ref+='1'
        else:
            ref+='0'
    ref = ref.split('0')
    for k in ref:
        if k: ans+=1

board = c_turn(board)
new_b = [''.join(i) for i in board]

for i in range(m):
    ref = ''
    for j in range(n):
        if new_b[i][j] == '|':
            ref+='1'
        else:
            ref+='0'
    ref = ref.split('0')
    for k in ref:
        if k: ans+=1

print(ans)