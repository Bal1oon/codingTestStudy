# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) > 1:
        scov1 = heapq.heappop(scoville)
        if scov1 >= K:
            return cnt
        scov2 = heapq.heappop(scoville)
        mixed = scov1 + scov2 * 2
        heapq.heappush(scoville, mixed)
        cnt += 1
        
    if scoville and scoville[0] >= K:
        return cnt
    
    return -1