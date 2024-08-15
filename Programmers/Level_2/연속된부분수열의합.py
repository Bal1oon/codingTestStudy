# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    start = 0
    cur_sum = 0
    shortest = -1
    
    for end in range(len(sequence)):
        cur_sum += sequence[end]
        
        while cur_sum >= k:
            if cur_sum == k:
                length = end - start + 1
                if shortest == -1 or length < shortest:
                    shortest = length
                    result = [start, end]
            cur_sum -= sequence[start]
            start += 1
            
    return result