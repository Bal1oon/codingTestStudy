# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    a, b = scores[0]
    s = a + b
    
    scores = sorted(scores, key = lambda x: (-x[0], x[1]))
    
    rank = 1
    max_b = 0
    
    for score in scores:
        if a < score[0] and b < score[1]:
            return -1
        if max_b <= score[1]:
            max_b = score[1]
            if sum(score) > s:
                rank += 1
            
    return rank

# A의 점수: [3, 2] (합 5)
# B의 점수: [2, 6] (합 8)
# C의 점수: [1, 5] (합 6)
## C의 점수가 A보다 높지만, B보다 값이 모두 작기 때문에 석차에 포함되지 않음
## B -> C -> A 로의 순위가 아닌 C가 탈락한 B -> A 가 됨
## 1번째 항, 2번째 항 모두 정렬