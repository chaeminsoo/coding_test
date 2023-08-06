# 2162
from collections import Counter

n = int(input())
segments = []
for _ in range(n):
    segments.append(list(map(int,input().split())))

parent = [i for i in range(n)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def outer_p(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def crossed(x1,y1,x2,y2,a1,b1,a2,b2):
    x_small, y_small, x_big, y_big = min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)
    a_small, b_small, a_big, b_big = min(a1,a2), min(b1,b2), max(a1,a2), max(b1,b2)

    if outer_p(x1,y1,x2,y2,a1,b1)*outer_p(x1,y1,x2,y2,a2,b2) == 0 and outer_p(a1,b1,a2,b2,x1,y1)*outer_p(a1,b1,a2,b2,x2,y2) == 0:
        if x_small <= a_big and y_small <= b_big and a_small <= x_big and b_small <= y_big:
            return True
    elif outer_p(x1,y1,x2,y2,a1,b1)*outer_p(x1,y1,x2,y2,a2,b2) <= 0 and outer_p(a1,b1,a2,b2,x1,y1)*outer_p(a1,b1,a2,b2,x2,y2) <= 0:
        return True
    return False

for i in range(n):
    seg_1 = segments[i]
    for j in range(i+1,n):
        seg_2 = segments[j]
        if crossed(seg_1[0],seg_1[1],seg_1[2],seg_1[3],seg_2[0],seg_2[1],seg_2[2],seg_2[3]):
            union_parent(parent,i,j)

for i in range(n):
    parent[i] = find_parent(parent,i)

print(len(set(parent)))
ans = 0
p_count = Counter(parent)
for i in p_count:
    ans = max(p_count[i],ans)
print(ans)