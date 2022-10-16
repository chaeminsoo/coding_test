# 14719
h,w = map(int, input().split())
hills = list(map(int, input().split()))

rain = 0
for i in range(1,w-1):
    left_hills = hills[:i]
    right_hills = hills[i+1:]

    l_max = max(left_hills)
    r_max = max(right_hills)

    ref = min(l_max, r_max)
    rain += max(ref-hills[i], 0)
print(rain) 