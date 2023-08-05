# 17387
a_x1, a_y1, a_x2, a_y2 = map(int,input().split())
b_x1, b_y1, b_x2, b_y2 = map(int,input().split())

def outer_p(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

a_xm, a_ym, a_xM, a_yM = min(a_x1,a_x2), min(a_y1,a_y2), max(a_x1,a_x2), max(a_y1,a_y2)
b_xm, b_ym, b_xM, b_yM = min(b_x1,b_x2), min(b_y1,b_y2), max(b_x1,b_x2), max(b_y1,b_y2)

# 한 직선
if outer_p(a_x1,a_y1,a_x2,a_y2,b_x1,b_y1)*outer_p(a_x1,a_y1,a_x2,a_y2,b_x2,b_y2) == 0 and outer_p(b_x1,b_y1,b_x2,b_y2,a_x1,a_y1)*outer_p(b_x1,b_y1,b_x2,b_y2,a_x2,a_y2) == 0:
    if a_xm <= b_xM and b_xm <= a_xM and a_ym <= b_yM and b_ym <= a_yM:
        print(1)
    else:
        print(0)
# 교차
elif outer_p(a_x1,a_y1,a_x2,a_y2,b_x1,b_y1)*outer_p(a_x1,a_y1,a_x2,a_y2,b_x2,b_y2) <= 0 and outer_p(b_x1,b_y1,b_x2,b_y2,a_x1,a_y1)*outer_p(b_x1,b_y1,b_x2,b_y2,a_x2,a_y2) <= 0:
    print(1)
else:
    print(0)