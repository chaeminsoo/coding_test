# https://school.programmers.co.kr/learn/courses/30/lessons/42895
def make_num(n,i):
    return int(str(n)*i)

def solution(N, number):
    if number == N:
        return 1
    
    dp = [[] for _ in range(9)]
    dp[1] = [N]
    for i in range(2,9):
        l = 1
        while l < i:
            r = i-l
            for ii in dp[l]:
                for jj in dp[r]:
                    if ii+jj == number:
                        return i
                    else:
                        dp[i].append(ii+jj)
                    
                    if ii-jj == number:
                        return i
                    else:
                        dp[i].append(ii-jj)
                        
                    if ii*jj == number:
                        return i
                    else:
                        dp[i].append(ii*jj)
                    
                    if jj != 0:
                        if ii/jj == number:
                            return i
                        else:
                            dp[i].append(ii/jj)
            l+=1
        dp[i].append(make_num(N,i))
        if make_num(N,i) == number:
            return i
    return -1