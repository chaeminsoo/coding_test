# 7490
t = int(input())

def solution(n,now,exp):
    if now > n:
        if eval(exp) == 0:
            ans.append(exp)
        return
    
    if exp[-1] in {'+', '_', '-'}:
        solution(n,now+1,exp+str(now))
    else:
        solution(n,now,exp+'+')
        solution(n,now,exp+'-')
        solution(n,now,exp+'_')


for _ in range(t):
    n = int(input())
    ans = []
    ref = solution(n,2,'1')
    rslt = []
    for i in ans:
        rslt.append(i.replace('_',' '))
    rslt.sort()
    for i in rslt:
        print(i)
    print()