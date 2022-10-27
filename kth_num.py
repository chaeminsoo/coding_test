# 1300
n = int(input())
k = int(input())

def num_count(num):
    global n
    cnt = 0
    for i in range(1,n+1):
        if num // i > 0:
            cnt += min(num//i, n)
        else:
            break
    return cnt

def bs(st,ed,k):
    global n
            
    mid = (st+ed)//2
    if st == mid:
        if num_count(st) == k:
            return st
        else:
            return st+1
    cnt = num_count(mid)

    if cnt >= k:
        return bs(st, mid, k)
    # elif cnt == k:
    #     return mid
    elif cnt < k:
        return bs(mid, ed, k)

print(bs(1,n**2,k))