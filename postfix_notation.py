# 1918
prefix = input()

stack = []
for i in prefix:
    if i not in {'+','-','*','/','(',')'}:
        print(i,end='')
        continue
    
    if not stack:
        stack.append(i)
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack:
                op = stack.pop()
                if op == '(':
                    break
                print(op,end='')
        else:
            while stack:
                if (stack[-1] in {'+','-'} and i in {'*','/'}) or stack[-1] == '(':
                    stack.append(i)
                    break
                op = stack.pop()
                print(op,end='')
            else:
                stack.append(i)

while stack:
    op = stack.pop()
    print(op,end='')