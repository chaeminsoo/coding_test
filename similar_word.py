# 2179
from collections import defaultdict

n = int(input())
words = []
for _ in range(n):
    words.append(input())

prefix_num = defaultdict(int)
prefix_word = defaultdict(list)
prefix_order = {}
max_pre = [0,'',1e9]
for idx in range(n):
    w = words[idx]
    prefix = ''
    for i in w:
        prefix += i
        prefix_num[prefix] += 1
        prefix_word[prefix].append(w)
        if prefix not in prefix_order:
            prefix_order[prefix] = idx

        if prefix_num[prefix] > 1 and len(prefix) > len(max_pre[1]):
            max_pre = [prefix_num[prefix],prefix,prefix_order[prefix]]
        elif prefix_num[prefix] > 1 and len(prefix) == len(max_pre[1]) and prefix_order[prefix] < max_pre[2]:
            max_pre = [prefix_num[prefix],prefix,prefix_order[prefix]]

if max_pre[0] == 0:
    for i in words[:2]:
        print(i)
else:
    for i in prefix_word[max_pre[1]][:2]:
        print(i)