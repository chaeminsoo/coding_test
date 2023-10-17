def solution(picks, minerals):
    can_mine = sum(picks)*5
    n = len(minerals)
    while n > can_mine:
        minerals.pop()
        n-=1    
    new_minerals = []
    ref = [0,0,0]
    cnt = 0
    for i in minerals:
        if i == 'diamond':
            ref[0]+=1
        elif i == 'iron':
            ref[1] += 1
        else:
            ref[2]+=1
        cnt+=1
        if cnt == 5:
            new_minerals.append(ref[:])
            ref = [0,0,0]
            cnt = 0
    if ref != [0,0,0]:
        new_minerals.append(ref[:])
        
    new_minerals.sort(reverse=True)
    ans = 0
    using_pick = 0
    pick_power = [[1,1,1],[5,1,1],[25,5,1]]
    flag = False
    
    for m in new_minerals:
        while picks[using_pick] <= 0:
            using_pick+=1
            if using_pick >= 3:
                flag = True
                break
        if flag:
            break
        for mi in range(3):
            ans += (pick_power[using_pick][mi]*m[mi])
        picks[using_pick]-=1
            
    return ans