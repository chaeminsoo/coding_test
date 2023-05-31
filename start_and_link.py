# 14889
from itertools import combinations

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
all_member = set(i for i in range(n))

all_a_team = list(combinations(all_member,n//2))

ans = 1e9

def cal_(a_team):
    b_team = all_member-a_team
    a_sum = 0
    for i in a_team:
        for j in a_team:
            a_sum += data[i][j]
    
    b_sum = 0
    for i in b_team:
        for j in b_team:
            b_sum += data[i][j]

    return abs(a_sum-b_sum)

for a_team in all_a_team:
    ans = min(ans,cal_(set(a_team)))

print(ans)