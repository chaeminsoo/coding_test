# 1406
import sys
input = sys.stdin.readline

stack = list(input().rstrip())
o = int(input().rstrip())

ref_stack = []
for _ in range(o):
    order = input().rstrip()
    if order[0] == 'L':
        if stack:
            ref = stack.pop()
            ref_stack.append(ref)
    elif order[0] == 'D':
        if ref_stack:
            ref = ref_stack.pop()
            stack.append(ref)
    elif order[0] == 'B':
        if stack:
            stack.pop()
    else:
        _, x = order.split()
        stack.append(x)    

print(''.join(stack) + ''.join(ref_stack[::-1]))