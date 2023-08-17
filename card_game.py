# 16566
from bisect import bisect_right

n,m,k = map(int,input().split())
cards = list(map(int,input().split()))
against_card = list(map(int,input().split()))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

parent = [i for i in range(m)]

cards.sort()
ans = []

for a in against_card:
    idx = bisect_right(cards,a)
    parent_idx = find_parent(parent,idx)
    ans.append(cards[parent_idx])
    if parent_idx+1 < m:
        union_parent(parent,parent_idx,parent_idx+1)

for i in ans:
    print(i)