# https://school.programmers.co.kr/learn/courses/30/lessons/131130?language=python3#
from collections import defaultdict

def solution(cards):
    n = len(cards)
    parent = [i for i in range(n+1)]
    
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
    
    for i in range(n):
        a = cards[i]
        b = cards[cards[i]-1]
        union_parent(parent,a,b)
    
    group_status = defaultdict(int)
    for i in range(n+1):
        parent[i] = find_parent(parent,i)
        group_status[parent[i]] += 1
        
    rslt = list(group_status.items())
    rslt.sort(key = lambda x:x[1])
    a = rslt[-1]
    b = rslt[-2]
    
    if b[0] == 0:
        return 0
    else:
        return a[1]*b[1]