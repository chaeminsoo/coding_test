# 9466
import sys
sys.setrecursionlimit(10**6)

t = int(input())

def solution(n,prefer_partner):
    global ans
    teamed = [0]*n
    ans = 0

    def dfs(st,now,passed,passed_check,pnt):
        global ans
        if teamed[now]:
            return

        if st == prefer_partner[now]:
            teamed[now] = 1
            pnt+=1
            ans += pnt
            return
        if now == prefer_partner[now]:
            teamed[now] = 1
            ans += 1
            return
        if prefer_partner[now] in passed_check:
            cnt = 0
            for p in passed:
                if p == prefer_partner[now]:
                    break
                cnt += 1
            pnt+=1
            teamed[now] = 1
            ans += pnt-cnt
            return
        
        pnt += 1
        teamed[now] = 1
        passed_check.add(now)
        passed.append(now)
        dfs(st,prefer_partner[now],passed,passed_check,pnt)
    
    for i in range(n):
        if teamed[i] == 0:
            dfs(i,i,[],set(),0)
    
    return n-ans

for _ in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    prefer_partner = []
    for i in data:
        prefer_partner.append(i-1)        
    print(solution(n,prefer_partner))