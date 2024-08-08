# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    heap = [-work for work in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        if heap:
            work = -heapq.heappop(heap)
            if work <= 0:
                break
            work -= 1
            heapq.heappush(heap, -work)
                
    answer = sum(work ** 2 for work in heap)
    return answer