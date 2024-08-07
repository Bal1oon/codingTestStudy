# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    n = len(triangle)
    d = [[0] * i for i in range(1, n+1)]
    d[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[i][j]
                
    answer = max(d[-1])
    return answer