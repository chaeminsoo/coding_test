n = int(input())
m = int(input())
loc = list(map(int,input().split()))

st = 1
ed = n
mid = (st+ed)//2
ans = 1e9
while st <= ed:
    light = [0]*(n+1)
    for i in loc:
        light[max(i-mid,0)] += 1
        light[min(i+mid,n)] -= 1
    
    for i in range(1,n+1):
        light[i] += light[i-1]
    
    if all(light[:-1]):
        ans = min(ans,mid)
        ed = mid-1
    else:
        st = mid+1

    mid = (st+ed)//2

print(ans)