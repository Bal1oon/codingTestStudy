# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    def max_sum(sticker):
        n = len(sticker)
        
        dp = [0] * n
        dp[0] = sticker[0]
        dp[1] = max(sticker[0], sticker[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
        
        return dp[-1]
        
    if len(sticker) <= 2:   # max_sum 함수 내에 if 문을 작성했을 시
        return max(sticker) # 런타임 에러가 발생하여 코드 동작을 줄이기 위해 함수 밖으로 꺼냄
    
    sum1 = max_sum(sticker[:-1])
    sum2 = max_sum(sticker[1:])
    
    answer = max(sum1, sum2)
    return answer