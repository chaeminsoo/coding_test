n = int(input())
m_loss = list(map(int,input().split()))
m_loss.sort()

max_loss = 0
if n%2 !=0:
    max_loss = m_loss.pop()
    n-=1

for i in range(n//2):
    ref = m_loss[i] + m_loss[n-i-1]
    max_loss = max(max_loss,ref)
print(max_loss)