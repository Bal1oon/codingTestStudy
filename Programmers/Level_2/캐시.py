# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    q = deque(maxlen = cacheSize)
    
    if cacheSize <= 0:
        return len(cities) * 5
    
    time = 0
    for city in cities:
        city = city.lower()
        
        # cache hit
        if city in q:
            q.remove(city)
            q.append(city)
            time += 1
        # cache miss
        else:
            q.append(city)
            time += 5
    
    return time