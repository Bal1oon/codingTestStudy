# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    n = len(money)

    if n <= 2:
        if n == 0:
            return 0
        return max(money)
        
    def theft(money):
        n = len(money)
        dp = [0] * n
        dp[0] = money[0]
        dp[1] = max(money[:2])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
        return dp[-1]

    sum1 = theft(money[:-1])
    sum2 = theft(money[1:])

    answer = max(sum1, sum2)
    return answer