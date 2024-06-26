# 1로 만들기
## 정수 X가 주어질 때 사용가능한 연산은 아래의 4가지이다.
## a. X가 5로 나누어 떨어지면, 5로 나눈다.
## b. X가 3으로 나누어 떨어지면, 3으로 나눈다.
## c. X가 2로 나누어 떨어지면, 2로 나눈다.
## d. X에서 1을 뺀다.
### 정수 X의 값 입력 (1 <= X <= 30000)
#### 연산을 하는 횟수의 최솟값 출력

def solution(x):
    d = [0] * 30001

    for i in range(2, x + 1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i-1] + 1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        # 현재의 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        # 현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    
    return d[x]

x = int(input())
s = solution(x)
print(s)