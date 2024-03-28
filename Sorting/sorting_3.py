# 두 배열의 원소 교체
## N개의 원소로 이뤄진 배열 A, B가 있을 때 최대 K번의 바꿔치기 연산을 수행해 모든 A의 원소 값을 더해 최댓값을 만들어라
### 1. N, K가 공백으로 주어짐
### 2. A의 원소가 공백으로 주어짐
### 3. B의 원소가 공백으로 주어짐

def solution(k, a, b):
    a.sort()
    b.sort(reverse = True)

    for i in range(k):
        if a[i] >= b[i]:
            break
        else:
            a[i], b[i] = b[i], a[i]
    
    return sum(a)

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = solution(k, a, b)
print(s)