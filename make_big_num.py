def solution(number, k):
    stack = []
    stack.append(number[0])
    for i in number[1:]:
        while stack and k and stack[-1] < i:
            stack.pop()
            k-=1
        stack.append(i)
    if k:
        return ''.join(stack)[:-k]
    else:
        return ''.join(stack)