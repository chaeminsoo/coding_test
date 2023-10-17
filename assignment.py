def change_t(t):
    h,m = t.split(':')
    h = int(h)
    m = int(m)
    return h*60 + m

def solution(plans):
    plans.sort(key = lambda x:x[1])
    ans = []
    stack = []
    prev_name = plans[0][0]
    prev_st = change_t(plans[0][1])
    prev_pt = int(plans[0][2])
    for name,st,pt in plans[1:]:
        st = change_t(st)
        pt = int(pt)
        if prev_st+prev_pt < st:
            ans.append(prev_name)
            while stack:
                s_name, s_pt = stack.pop()
                if prev_st+prev_pt+s_pt <= st:
                    ans.append(s_name)
                    prev_pt += s_pt
                else:
                    left_t = prev_st+prev_pt+s_pt-st
                    stack.append([s_name,left_t])
                    break
                
        elif prev_st+prev_pt == st:
            ans.append(prev_name)
        else:
            left_t = prev_st+prev_pt - st
            stack.append([prev_name,left_t])
        
        prev_name = name
        prev_st = st
        prev_pt = pt
    
    ans.append(name)
    while stack:
        ref = stack.pop()
        ans.append(ref[0])
    
    return ans