# 17420
import math

n = int(input())
As = list(map(int,input().split()))
Bs = list(map(int,input().split()))

gifty = list(zip(As,Bs))

gifty.sort(key= lambda x: (x[1],x[0]))

day_max = gifty[0][1]
now_max = 0
prev_max = 0
ans = 0

for due, day in gifty:
    if day_max != day:
        day_max = day
        prev_max = now_max
        now_max = 0

    if due < day_max:
        ref = math.ceil((day_max-due)/30)
        due+=(30*ref)
        ans+=ref
    if due < prev_max:
        ref = math.ceil((prev_max-due)/30)
        due+=(30*ref)
        ans+=ref
    
    now_max = max(now_max, due)
print(ans)