# 숫자 카드 게임
## 숫자가 쓰인 카드들이 N x M 형태로 놓여있다.
## 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다. 
## 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
## 따라서 처음에 카드를 골라낼 행을 선택할 떄, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
### 첫째 줄에 행의 개수 N과 열의 개수 M이 공백을 기준으로, 각각 자연수로 주어진다.
### 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다.
#### 선택한 카드의 적힌 숫자 출력

def solution(n, m, cards):
    min_ls = list()
    for i in range(n):
        min_ls.append(min(cards[i]))
    return max(min_ls)

n, m = map(int, input().split())
cards = list()
for i in range(n):
    l = list(map(int, input().split()))
    cards.append(l)

s = solution(n, m, cards)
print(s)