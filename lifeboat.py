def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    c1, c2 = 0, len(people)-1
    pnt = 0
    while c1 < c2:
        if people[c1] + people[c2] <= limit:
            c1+=1
            c2-=1
            pnt+=2
            answer+=1
        else:
            c1+=1
            pnt+=1
            answer+=1    
    if pnt < len(people):
        answer+=1
    return answer