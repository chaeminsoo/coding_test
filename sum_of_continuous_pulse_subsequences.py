# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence):
    n = len(sequence)
    seq_1 = []
    seq_2 = []
    ref = 1
    for i in sequence:
        seq_1.append(i*ref)
        ref*=-1
        seq_2.append(i*ref)
    
    dp_1 = [0]*n
    dp_1[0] = seq_1[0]
    for i in range(1,n):
        dp_1[i] = max(seq_1[i],dp_1[i-1]+seq_1[i])
    dp_2 = [0]*n
    dp_2[0] = seq_2[0]
    for i in range(1,n):
        dp_2[i] = max(seq_2[i],dp_2[i-1]+seq_2[i])
    
    return max(max(dp_1),max(dp_2))