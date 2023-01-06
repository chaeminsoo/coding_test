# 8983
import sys
input = sys.stdin.readline
from bisect import bisect_left

m, n, l = map(int,input().split())
shooters = list(map(int,input().split()))
shooters.sort()
animals = []
for _ in range(n):
    a,b = map(int,input().split())
    if b > l:
        continue
    animals.append((a,b))

def find_nearest(l, v):
    idx = bisect_left(l,v)
    if idx == 0:
        return l[0]
    if idx == len(l):
        return l[-1]
    if l[idx] - v < v - l[idx-1]:
        return l[idx]
    return l[idx-1]

cnt = 0
for x,y in animals:
    idx = find_nearest(shooters,x)
    if abs(idx-x) + y >l:
        continue
    else:
        cnt+=1
print(cnt)