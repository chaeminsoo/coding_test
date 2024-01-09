# https://school.programmers.co.kr/learn/courses/30/lessons/258707?language=python3
def solution(coin, cards):
    n = len(cards)
    num_idx = {j:i for i,j in enumerate(cards)}
    used = [False]*n
    
    hands = n//3
    
    flag = True
    turns = 1
    while flag:
        flag = False
        available = hands+(2*turns)
        if available > n:
            break
            
        for i in range(available):
            if used[i]:
                continue
                
            need_num = n - cards[i] +1
            
            if need_num in num_idx:
                if num_idx[need_num] <= available-1:
                    if i < hands and num_idx[need_num] < hands:
                        flag = True
                        turns+=1
                        used[i] = True
                        used[num_idx[need_num]] = True
                        break
                    elif i < hands and num_idx[need_num] >= hands:
                        if coin > 0:
                            flag = True
                            turns+=1
                            coin-=1
                            used[i] = True
                            used[num_idx[need_num]] = True
                            break
                    elif i >= hands and num_idx[need_num] >= hands:
                        if coin >= 2:
                            flag = True
                            turns+=1
                            coin-=2
                            used[i] = True
                            used[num_idx[need_num]] = True
                            break
                            
    return turns