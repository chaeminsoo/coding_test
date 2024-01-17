# https://school.programmers.co.kr/learn/courses/30/lessons/147354?language=python3
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x:(x[col-1],-x[0]))
    s_i = []
    for i in range(row_begin-1, row_end):
        rslt = 0
        for c in data[i]:
            rslt += c%(i+1)
        s_i.append(rslt)
    ans = s_i[0]
    for i in s_i[1:]:
        ans ^= i
    return ans