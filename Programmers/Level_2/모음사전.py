# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    vowels = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    
    result = 0
    for i in range(len(word)):
        val = vowels[word[i]]
        result += val + sum([5**j for j in range(1, 5-i)]) * (val - 1)
    return result


## e.g. EIO
## E - 2 + (5^1 + 5^2 + 5^3 + 5^4) * (2 - 1)
## I - 3 + (5^1 + 5^2 + 5^3) * (3 - 1)
## O - 4 + (5^1 + 5^2) * (4 - 1)