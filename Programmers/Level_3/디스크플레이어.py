# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    jobs.sort()
    
    i = 0
    complete = 0
    cur_time = 0
    total_req_to_end = 0
    heap = []
    
    while complete < len(jobs):
        while i < len(jobs) and jobs[i][0] <= cur_time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if heap:
            duration, req_time = heapq.heappop(heap)
            cur_time += duration
            total_req_to_end += cur_time - req_time
            complete += 1
        else:
            cur_time = jobs[i][0]
            
    answer = total_req_to_end // len(jobs)
    return answer