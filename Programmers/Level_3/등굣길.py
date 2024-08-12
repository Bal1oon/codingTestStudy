# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    puddles_set = set((j-1, i-1) for i, j in puddles)

    for i in range(n):
        for j in range(m):
            if (i, j) in puddles_set:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[n-1][m-1] % 1000000007