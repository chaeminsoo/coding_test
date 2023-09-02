# 2020 카카오 인턴십 보석 쇼핑
def solution(gems):
    ans = [1e9,1e9,1e9]
    n = len(gems)
    gem_num = len(set(gems))
    gem_status = 0
    all_gem = 2**gem_num-1
    
    gem_dict = {j:i for i,j in enumerate(set(gems))}
    gem_how_many = {i:0 for i in gems}
    
    cur_1 = 0
    cur_2 = 0
    gem_how_many[gems[cur_1]] += 1
    gem_status |= 1<<gem_dict[gems[cur_1]]
    while cur_2 < n and cur_1 <= cur_2:
        if gem_status != all_gem:
            if cur_2 < n-1:
                cur_2 += 1
                gem_status |= 1<<gem_dict[gems[cur_2]]
                gem_how_many[gems[cur_2]]+=1
            else:
                break
        else:
            if cur_2-cur_1+1 < ans[2]:
                ans = [cur_1+1,cur_2+1,cur_2-cur_1+1]
            elif cur_2-cur_1+1 == ans[2] and cur_1+1 < ans[0]:
                ans = [cur_1+1,cur_2+1,cur_2-cur_1+1]

            gem_how_many[gems[cur_1]] -= 1
            if gem_how_many[gems[cur_1]] == 0:
                gem_status -= 1<<gem_dict[gems[cur_1]]
            cur_1 += 1
        
    return ans[:2]