# https://school.programmers.co.kr/learn/courses/30/lessons/132265#
from collections import defaultdict

def solution(topping):
    all_topping = len(set(topping))
    ans = 0
    top_status = defaultdict(int)
    ref = set()
    for i in topping:
        top_status[i] += 1

    for i in topping:
        ref.add(i)
        top_status[i] -= 1
        if top_status[i] == 0:
            all_topping -= 1

        if len(ref) == all_topping:
            ans+=1

    return ans