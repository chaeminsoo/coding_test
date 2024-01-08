# https://school.programmers.co.kr/learn/courses/30/lessons/258705?language=python3
# 2024 카카오 겨울 인턴 기출문제

# "역방향 삼각형을 어떻게 채울것인가"에 집중
def solution(n, tops):
    # k번째 아래 방향 정삼각형을 덮는 방법이 3번 방법인 경우의 수
    a = [0]*(n+1)
    # k번째 아래 방향 정삼각형을 덮는 방법이 3번 방법이 아닌 경우의 수
    b = [0]*(n+1)
    
    a[1] = 1
    if tops[0]:
        b[1] = 3
    else:
        b[1] = 2
    
    for k in range(2,len(tops)+1):
        if tops[k-1]:
            a[k] = (a[k-1] + b[k-1])%10007
            b[k] = (2*a[k-1] + 3*b[k-1])%10007
        else:
            a[k] = (a[k-1] + b[k-1])%10007
            b[k] = (a[k-1] + 2*b[k-1])%10007
    
    return (a[n]+b[n])%10007