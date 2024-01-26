# 2668
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
nums = {}
num_status = defaultdict(int)
under = set()
for i in range(n):
    num_status[i+1] += 1
    ref = int(input())
    num_status[ref] += 1
    under.add(ref)
    nums[i+1] = ref
    
flag = True
while flag:
    flag = False
    for i in num_status:
        if num_status[i] == 1:
            flag = True
            num_status[i] -= 1
            num_status[nums[i]] -= 1
    
ans = []
for i in num_status:
    if num_status[i] != 0:
        ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
    print(i)