# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = []
    gems_num = len(set(gems))
    start = 0
    gems_dict = {}
    shortest = 100001
    
    for end in range(len(gems)):
        gems_dict[gems[end]] = gems_dict.get(gems[end], 0) + 1
        
        while gems_num == len(gems_dict):
            length = end - start + 1
            if length < shortest:
                shortest = length
                answer = [start+1, end+1]
                
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            
    return answer