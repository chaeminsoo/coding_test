# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    ans = 0
    wn = len(want)
    dn = len(discount)
    status_set = set()
    status = {}
    target_num = {}
    for i in range(wn):
        status[want[i]] = 0
        target_num[want[i]] = number[i]
        
        
    for i in range(10):
        if discount[i] in status:
            status[discount[i]] += 1
            if status[discount[i]] >= target_num[discount[i]]:
                status_set.add(discount[i])
            if len(status_set) == wn:
                ans += 1
    
    
    st = 0
    ed = 9
    while ed <= dn:
        try:
            if discount[st] in status:
                status[discount[st]] -= 1
                if status[discount[st]] < target_num[discount[st]]:
                    try:
                        status_set.remove(discount[st])
                    except KeyError:
                        pass
            st+=1
            ed+=1
            if discount[ed] in status:
                status[discount[ed]] += 1
                if status[discount[ed]] >= target_num[discount[ed]]:
                    status_set.add(discount[ed])

            if len(status_set) == wn:
                ans += 1
        except IndexError:
            break
        
    return ans