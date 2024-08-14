# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    if len(topping) == 1:
        return 0

    answer = 0
    left = set()
    right = Counter(topping)
    
    for i in range(len(topping)):
        t = topping[i]
        left.add(t)
        right[t] -= 1
        
        if right[t] <= 0:
            del right[t]
        if len(left) == len(right):
            answer += 1
    
    return answer