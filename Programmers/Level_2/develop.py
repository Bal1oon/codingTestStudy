# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math

def solution(progresses, speeds):
    q = deque()
    for p, s in zip(progresses, speeds):
        x = math.ceil( (100-p) / s )
        q.append(x)
    
    result = []
    count = 0
    
    while q:
        deploy = q.popleft()
        count = 1
        
        while q and q[0] <= deploy:
            q.popleft()
            count += 1
        result.append(count)
        
    return result