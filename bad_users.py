def solution(user_id, banned_id):
    n = len(banned_id)
    banned_case = [[] for _ in range(len(banned_id))]
    for bidx, bid in enumerate(banned_id):
        for uid in user_id:
            if len(uid) == len(bid):
                flag = True
                for i in range(len(uid)):
                    if bid[i] != "*" and uid[i] != bid[i]:
                        flag = False
                        break
                if flag:
                    banned_case[bidx].append(uid)
    
    ans = []
    def dfs(idx,case,n):
        if idx >= n:
            if case not in ans:
                ans.append(case)
            return
        
        for bid in banned_case[idx]:
            if bid not in case:
                dfs(idx+1,case|{bid},n)
    
    dfs(0,set(),n)
    return len(ans)