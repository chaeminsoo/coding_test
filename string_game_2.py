# 20437
from collections import defaultdict

def solution(w,k):
    ans_1 = 1e9
    ans_2 = 0

    how_many = defaultdict(int)
    where = defaultdict(list)
    for i in range(len(w)):
        how_many[w[i]] += 1
        where[w[i]].append(i)
    
    candi = []
    for i in how_many:
        if how_many[i] >= k:
            candi.append(i)

    if candi:
        for c in candi:
            for i in range(len(where[c])):
                try:
                    ans_1 = min(where[c][i+k-1] - where[c][i] + 1,ans_1)
                    ans_2 = max(where[c][i+k-1] - where[c][i] + 1,ans_2)
                except IndexError:
                    pass

        return ans_1, ans_2
    else:
        return -1
    
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    ans = solution(w,k)
    if ans == -1:
        print(-1)
    else:
        print(*ans)