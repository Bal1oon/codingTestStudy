# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    
    def conv(n, q):
        digit = ''
        while n > 0:
            n, mod = divmod(n, q)
            if mod >= 10:
                mod = chr(mod - 10 + ord('A'))
            digit += str(mod)
        return digit[::-1]
    
    digit = '0'
    k = t * m
    for i in range(k):
        digit += conv(i, n)
    
    for i in range(p-1, len(digit), m):
        answer += digit[i]
        if len(answer) == t:
            break
    
    return answer