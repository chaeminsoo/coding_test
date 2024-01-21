# https://school.programmers.co.kr/learn/courses/30/lessons/135807?language=python3
from math import gcd

def solution(arrayA, arrayB):
    all_num = set(arrayA+arrayB)
    
    a_gcd = arrayA[0]
    for i in arrayA:
        a_gcd = gcd(a_gcd,i)
        
    b_gcd = arrayB[0]
    for i in arrayB:
        b_gcd = gcd(b_gcd,i)
    
    ans = [0]
    flag = False
    for a in arrayA:
        if a%b_gcd == 0:
            flag = True
            break
    if not flag:
        ans.append(b_gcd)
    
    flag = False
    for b in arrayB:
        if b%a_gcd == 0:
            flag = True
            break
    if not flag:
        ans.append(a_gcd)
    
    return max(ans)
            