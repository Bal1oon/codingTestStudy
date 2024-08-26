# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def solution(user_id, banned_id):
    num_u = len(user_id)
    num_b = len(banned_id)
    cases = set()
    
    def mapping(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if u != b and b != '*':
                return False
        return True
        
    for perm in permutations(user_id, num_b):
        if all(mapping(perm[i], banned_id[i]) for i in range(num_b)):
            cases.add(tuple(sorted((perm))))
    
    result = len(cases)
    return result