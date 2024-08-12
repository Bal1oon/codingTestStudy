# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()
    
    i = 0
    cnt = 0
    for a in A:
        if i >= len(B):
            break
        for j in range(i, len(B)):
            if a < B[i]:
                cnt += 1
                i += 1
                break
            i += 1
                
    return cnt