# https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=python3
def solution(elements):
    n = len(elements)
    rslt = set()
    for i in elements:
        rslt.add(i)
    
    for i in range(1,n):
        st = 0
        ed = st+i
        ref = 0
        for j in range(st,ed+1):
            ref += elements[j]
        rslt.add(ref)
        while st < n:
            st%=n
            ref -= elements[st]
            st+=1
            ed = (ed+1)%n
            ref+= elements[ed]
            rslt.add(ref)
            
    return len(rslt)