# 7682
def win_game(data,ox):
    cnt = 0
    if data[0] == ox and data[0] == data[1] == data[2]: # 첫번째 가로줄 완성
        cnt+=1 # return True
    if data[3] == ox and data[3] == data[4] == data[5]: # 두첫번째 가로줄 완성
        cnt+=1 # return True
    if data[6] == ox and data[6] == data[7] == data[8]: # 세번째 가로줄 완성
        cnt+=1 # return True

    if data[0] == ox and data[0] == data[3] == data[6]: # 첫번째 세로줄 완성
        cnt+=1 # return True
    if data[1] == ox and data[1] == data[4] == data[7]: # 두첫번째 세로줄 완성
        cnt+=1 # return True
    if data[2] == ox and data[2] == data[5] == data[8]: # 세번째 세로줄 완성
        cnt+=1 # return True

    if data[0] == ox and data[0] == data[4] == data[8]: # 오른쪽 아래 대각선 완성
        cnt+=1 # return True
    if data[6] == ox and data[6] == data[4] == data[2]: # 왼쪽 아래 대각선 완성
        cnt+=1 # return True

    if cnt == 1:
        return True
    else:
        return False

    # else: return False # 못이김

def checking(data):
    x_num = data.count('X')
    o_num = data.count('O')
    if o_num == x_num:
        if win_game(data,'O') and not win_game(data,'X'):
            return 'valid'
        else:
            return 'invalid'
    elif o_num + 1 == x_num:
        if win_game(data, 'X') and not win_game(data, 'O'):
            return 'valid'
        elif win_game(data, 'X') and win_game(data, 'O'):
            return 'invalid'
        elif not win_game(data, 'X') and win_game(data, 'O'):
            return 'invalid'
        elif not win_game(data, 'X') and not win_game(data, 'O'):
            if x_num + o_num == 9:
                return 'valid'
            else:
                return 'invalid'
    else:
        return 'invalid'

while True:
    data = input()
    if data == 'end':
        break
    else:
        print(checking(data))