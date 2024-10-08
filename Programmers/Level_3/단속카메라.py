# https://school.programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    routes.sort(key = lambda x:x[1])
    camera = routes[0][1]
    answer = 1
    
    for route in routes:
        if route[0] > camera:
            camera = route[1]
            answer += 1
    
    return answer