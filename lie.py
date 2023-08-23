# 1043
from copy import deepcopy

n,m = map(int,input().split())

know_the_truth = list(map(int,input().split()))
if know_the_truth[0] == 0:
    print(m)
    exit()
else:
    know_the_truth = set(know_the_truth[1:])

party = []
for i in range(m):
    data = list(map(int,input().split()))
    num = data[0]
    ppl = set(data[1:])
    if len(ppl&know_the_truth) != 0:
        know_the_truth |= ppl
    party.append(ppl)

new_truth = deepcopy(know_the_truth)
while True:
    for p in party:
        if len(new_truth&p) != 0:
            new_truth |= p
    if new_truth == know_the_truth:
        break
    know_the_truth = deepcopy(new_truth)

ans = 0
if len(know_the_truth) == n:
    print(0)
else:
    for p in party:
        if len(p&know_the_truth) == 0:
            ans+=1
    print(ans)