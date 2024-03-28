# 위에서 아래로
## 수열을 내림차순으로 정렬하는 프로그램을 만드시오
### 첫째 줄에 수열에 속해 있는 수의 개수 N
### 둘째 줄부터 N+1번째 줄까지 N개의 수 입력
#### 내림차순으로 정렬된 결과를 공백으로 구분하여 출력

def solution(n, arr):
    arr.sort(reverse=True)
    for e in arr:
        print(e, end=' ')

n = int(input())
arr = [int(input()) for _ in range(n)]

solution(n, arr)
