# 17214
poly = input()
ans = ''

nums = set(str(i) for i in range(10))
elements = []


ref_num = ''
xnt = 0
for i in poly:
    if i in nums:
        ref_num += i
    elif i == 'x':
        xnt += 1
    else:
        if ref_num =='0':
            continue
        elif ref_num:
            elements.append([int(ref_num), xnt])
        elif xnt != 0:
            elements.append([1, xnt])
        ref_num = ''
        xnt = 0
        elements.append(i)

if ref_num =='0':
    pass
elif ref_num:
    elements.append([int(ref_num), xnt])
elif xnt != 0:
    elements.append([1, xnt])

for e in elements:
    if type(e) is not list:
        ans += e
    else:
        num, xnt = e
        xnt+=1
        num//=xnt
        if num != 1:
            ans+=str(num)
        ans+=('x'*xnt)
if ans:
    ans+='+W'
else:
    ans+='W'
print(ans)