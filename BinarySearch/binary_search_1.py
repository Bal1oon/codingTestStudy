# 부품 찾기
## 매장의 부품 N개가 있고, 손님이 M개의 부품을 요청했을 때 부품이 있는지 확인하는 프로그램을 작성하라
### 1. 매장의 부품 N
### 2. N개의 부품 번호, 공백으로 구분
### 3. 손님이 요천한 부품 개수 M
### 4. M개의 부품 번호, 공백으로 구분
#### 공백으로 구분하여 각 부품에 대해 yes, no를 출력

def solution(n, store, m, requests):
    for e in requests:
        result = binary_search(store, e, 0, n-1)
        print(result, end=' ')

def binary_search(arr, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if arr[mid] == target:
        return 'yes'
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

n = int(input())
store = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

solution(n, store, m, requests)