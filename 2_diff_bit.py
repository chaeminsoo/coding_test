# https://school.programmers.co.kr/learn/courses/30/lessons/77885#
def solution(numbers):
    ans = []
    for n in numbers:
        if n%2 == 0:
            ans.append(n+1)
        else:
            num = list(bin(n)[2:])
            flag = False
            n = len(num)
            for i in range(n-1,-1,-1):
                if num[i] == '0':
                    num[i] = '1'
                    num[i+1] = '0'
                    flag = True
                    break
            if flag:
                ans.append(int(''.join(num),2))
            else:
                num[0] = '10'
                ans.append(int(''.join(num),2))
    return ans