# 10815
from bisect import bisect_left

n = int(input())
hand_cards = list(map(int,input().split()))
m = int(input())
check_cards = list(map(int,input().split()))

ans = []
hand_cards.sort()
for c in check_cards:
    idx = bisect_left(hand_cards, c)
    if idx == n:
        ans.append(0)
    else:
        if hand_cards[idx] == c:
            ans.append(1)
        else:
            ans.append(0)
for i in ans:
    print(i,end=' ')