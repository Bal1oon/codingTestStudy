# 금광
## n x m 크기의 금광이 있을 때 각 칸에는 특정한 크기의 금이 있다.
## 채굴자는 첫 번째 열부터 출발하며 어느 행에서든 출발할 수 있다.
## m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 움직일 때 얻을 수 있는 금의 최대 크기를 구하라
## 가장 왼쪽 위를 (1, 1), 가장 오른쪽 아래의 위치를 (n, m)이라 한다
### 첫째줄 테스트 케이스 T 입력 (1 <= T <= 1000)
### 매 테스트 케이스 첫째줄에 n, m 공백 구분으로 입력 (1 <= n, m <= 20)
### 매 테스트 케이스 둘째줄에 n x m개의 금의 개수 공백으로 구분하여 입력 (0 <= 금 <= 100)
#### 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력
#### 각 테스트 케이스마다 줄 바꿈을 이용해 출력

def solution(n, m, golds):
    ## a_ij = max(a_[i-1][j-1], a_[i][j-1], a_[i+1][j-1]) + mine[i][j]
    d = [[0] * m for _ in range(n)]

    d[0][0] = golds[0][0]
    d[1][0] = golds[1][0]
    d[2][0] = golds[2][0]

    for j in range(1, m):
        for i in range(n):
            right_up, right, right_down = 0, 0, 0
            if i-1 < 0:
                d[i][j] = max(d[i][j-1], d[i+1][j-1]) + golds[i][j]
            elif i+1 >= n:
                d[i][j] = max(d[i-1][j-1], d[i][j-1]) + golds[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + golds[i][j]

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    return result

t = int(input())
result = []
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    golds = []
    for _ in range(n):
        golds.append(array[:m])
        array = array[m:]
        
    s = solution(n, m, golds)
    result.append(s)

for r in result:
    print(r)