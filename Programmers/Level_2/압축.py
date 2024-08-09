# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from collections import deque

def solution(msg):
    dic = dict()
    for i in range(26):
        dic[chr(i+65)] = i+1

    q = deque(msg)
    w = ''
    index = 27
    answer = []

    while q:
        w += q.popleft()
        if w not in dic:
            dic[w] = index
            index += 1
            answer.append(dic[w[:-1]])
            w = w[-1]

    answer.append(dic[w])
    return answer