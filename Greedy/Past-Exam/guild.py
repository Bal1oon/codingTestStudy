# 모험가 길드
## 모험가 N명의 '공포도'를 측정했다.
## '공포도'가 X인 모험가는 반드시 X명 이상으로 그룹을 이뤄야 여행을 떠날 수 있다
## 모험가 N명이 있을 때 최대 몇개의 모험가 그룹을 만들 수 있는지 구하라
### 모험가의 수 N 입력 (1 <= N <= 100,000)
### 공포도의 값을 N 이하의 자연수로 입력
#### 그룹 수의 최댓값 출력

n = int(input())
fear = list(map(int, input().split()))
fear = sorted(fear)

num_soldier = 0
num_group = 0

for i in fear:
    num_soldier += 1
    if i <= num_soldier:
        num_group += 1
        num_soldier = 0

print(num_group)