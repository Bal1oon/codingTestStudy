# 정수 삼각형
## 정수로 이뤄진 삼각형이 있을 때, 맨 위층부터 시작해 아래에 있는 수 중 하나를 택해 아래층으로 내려오며 선택한 수의 합이 최대가 되도록 작성하시오.
## 아래층에 있는 수는 현재 층에서 대각선 왼쪽 또는 대각선 오른쪽에 있는 것만 선택 가능하다.
## 삼각형의 크기는 1 이상 500 이하이다
## 삼각형 안에 정수의 크기는 0 이상 9999 이하이다.
### 삼각형의 크기 n 입력
### n개의 줄로 이뤄진 정수 삼각형 입력
#### 합의 최댓값 출력

def solution(n, triangle):
    ## 가장 왼쪽 항의 경우(첫번째 index) row 계속 줄어듦, col 그대로 
    ## 가장 오른쪽 항의 경우 (마지막 index) row 계속 줄어듦, col 줄어듦
    ## 중간 항들 row 계속 줄어듦, col 그대로거나 줄어듦

    ## a[i][j] = max(a[i-1][j], a[i-1][j-1]) + triangle[i][j]

    # 삼각형 크기와 똑같은 크기로 초기화
    d = [[0] * i for i in range(1, n+1)]
    d[0][0] = triangle[0][0]    # 첫 항은 항상 같음

    for i in range(1, n):
        for j in range(len(d[i])):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == len(d[i]) - 1:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j], d[i-1][j-1]) + triangle[i][j]

    result = max(d[n-1])
    
    return result

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

s = solution(n, triangle)
print(s)