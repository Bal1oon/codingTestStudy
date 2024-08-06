# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key = lambda x : len(x))
    
    answer = []
    for i in s:
        m = list(map(int, i.split(',')))
        n = [item for item in m if item not in answer]
        answer.append(n[0])
    return answer