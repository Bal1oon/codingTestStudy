# 1이 될 때까지
## 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
## N에서 1을 뺀다.
## N을 K로 나눈다.
### 첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
#### 첫째 줄에 N이 1이 될 때까지 과정을 수행하는 횟수의 최솟값을 출력한다.

def solution(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1
    return count

n, k = map(int, input().split())
s = solution(n, k)

print(s)