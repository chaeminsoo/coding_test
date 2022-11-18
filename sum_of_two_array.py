# 2143
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

ans = 0
dict_a = {}
for i in range(n):
    for j in range(1,n):
        ref = sum(a[i:i+j])
        try:
            dict_a[ref] += 1
        except KeyError:
            dict_a[ref] = 1

checks = {}
for i in range(m):
    for j in range(1,m):
        ref = sum(b[i:i+j])
        try:
            checks[ref]
            continue
        except:
            checks[ref] = True
        ref2 = t -ref
        try:
            ans += dict_a[ref2]
        except KeyError:
            pass
print(ans)     