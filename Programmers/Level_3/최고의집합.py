# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    
    q, r = s//n, s%n
    answer = [q for i in range(n-r)] + [q+1 for i in range(r)]
    return answer