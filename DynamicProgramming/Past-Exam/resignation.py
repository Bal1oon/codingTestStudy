# 퇴사
## N+1일 째 되는 날 퇴사를 하려고 할 때, 남은 N일 동안 상담원으로서 최대한 많은 상담을 하려고 한다.
## 각각의 상담은 상담을 완료하는 데 결리는 기간 Ti와 상담 후 받는 금액 Pi로 이루어져 있다.
## 상담이 이뤄지면 Ti의 기간동안 다른 상담을 하지 못하며, N+1일째에는 회사에 없기 때문에 N+1일에 걸친 기간의 상담은 할 수 없다.
## 상담을 적절히 했을 때, 얻을 수 있는 최대 수익을 구하라
### N 입력 (1 <= N <= 15)
### Ti와 Pi가 공백으로 구분되어 1~N일까지 한줄씩 입력된다 (1 <= Ti <= 5, 1 <= Pi <= 1000)
#### 최대 이익 출력

def solution(n, times, pays):
    ## N+1일을 초과하는 경우가 있기 때문에 순서를 역으로 함
    ## a[i] = a[i-T[i]] + P[i]

    d = [0] * n
    times = times[::-1]
    pays = pays[::-1]

    for i in range(n):
        if i - times[i] < -1:   # 시작 인덱스가 0이기 때문에 1일 근무 시 -1이 최솟값이 됨
            continue            # 근무 일수가 N+1일을 넘으면 계산하지 않음
        d[i] = d[i - times[i]] + pays[i]
    
    return max(d)

n = int(input())
times, pays = [], []
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)

s = solution(n, times, pays)
print(s)