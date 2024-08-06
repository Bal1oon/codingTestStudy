# https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    def get_sub(s):
        s = s.lower()
        sub = []
        for i in range(len(s)-1):
            if 97 <= ord(s[i]) <= 122 and 97 <= ord(s[i+1]) <= 122:
                sub.append(s[i:i+2])
        return sub
    
    a = Counter(get_sub(str1))
    b = Counter(get_sub(str2))
    
    intersection = sum((a & b).values())
    union = sum((a | b).values())
    
    if union == 0:
        return 65536
    return int(intersection / union * 65536)