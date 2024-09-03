# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        learned = ''
        
        for s in tree:
            if s in skill:
                learned += s
                
        if skill.startswith(learned):
            answer += 1
            
    return answer