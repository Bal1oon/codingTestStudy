# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# stack/queue

from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    while q:
        p = q.popleft()
        if any(p[0] < r[0] for r in q):
            q.append(p)
        else:
            answer += 1
            if p[1] == location:
                break
    
    return answer