# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        cmd, data = op.split()
        data = int(data)
        if cmd == 'I':
            heapq.heappush(min_heap, data)
            heapq.heappush(max_heap, -data)
        elif cmd == 'D':
            if data == 1 and min_heap:
                min_heap.remove(-heapq.heappop(max_heap))
            elif data == -1 and max_heap:
                max_heap.remove(-heapq.heappop(min_heap))
    
    if not min_heap:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]