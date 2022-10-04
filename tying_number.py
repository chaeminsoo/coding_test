# 1744
n = int(input())
p_nums = []
m_nums = []
z = 0
ans = 0
for _ in range(n):
    num = int(input())
    if num == 1:
        ans+=1
    elif num > 0:
        p_nums.append(num)
    elif num < 0:
        m_nums.append(num)
    else:
        z+=1

if len(p_nums) % 2 != 0: p_nums.append(1)
if len(m_nums) % 2 != 0: m_nums.append(1)
p_nums.sort()
m_nums.sort(reverse=True)
while p_nums:
    i = p_nums.pop()
    j = p_nums.pop()
    ans += (i*j)
while m_nums:
    i = m_nums.pop()
    j = m_nums.pop()
    ref = (i*j)
    if ref >= 0:
        ans+=ref
    else:
        if z > 0:
            z-=1
        else:
            ans += ref
print(ans)