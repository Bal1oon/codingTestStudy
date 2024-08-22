# https://school.programmers.co.kr/learn/courses/30/lessons/12979

import math

def solution(n, stations, w):
    left = 0
    answer = 0
        
    if not stations:
        answer = math.ceil(n / (w * 2 + 1))
        return answer
    
    for right in stations:
        right -= w
        if right > left + 1:
            answer += math.ceil((right - left - 1) / (w * 2 + 1))
        left = right + w * 2
    
    if n >= left:
        answer += math.ceil((n - left) / (w * 2 + 1))
    
    return answer