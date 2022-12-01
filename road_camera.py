# https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=python3
def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    camera_spot = -30000
    
    for car_in, car_out in routes:
        if camera_spot < car_in:
            camera_spot = car_out
            answer+=1
    return answer