# 효율적인 화폐 구성
## N가지 종류의 화폐에서 최소한의 개수로 합이 M원이 되도록 한다.
## 각 화폐는 무제한으로 사용 가능하며 화폐 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
### 1. N, M 입력 (1 <= N <= 100, 1 <= M <= 10000)
### 2. N개의 줄로 화폐의 가치 입력
#### M원을 만들기 위한 최소한의 화폐 개수 출력
#### 불가능 시 -1 출력

def solution(n, m, coins):
    # m의 최대 크기가 10,000이기 때문에 만들 수 없는 경우로서 10,001로 초기화
    d = [10001] * (m+1)
    d[0] = 0

    ## 2와 3이 있을 때 m을 만들기 위해서는 m-2와 m-3을 만드는 최소 개수 중 더 작은 값에 1을 더한 값이다 -> min(a_i, a_(i-k) + 1)
    for i in range(n):
        for j in range(coins[i], m+1):
            if d[j - coins[i]] != 10001:
                d[j] = min(d[j], d[j - coins[i]] + 1)
    
    return d[m]

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

s = solution(n, m, coins)
if s == 10001:
    print(-1)
else:
    print(s)