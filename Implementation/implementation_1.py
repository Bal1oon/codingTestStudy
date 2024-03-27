# 왕실의 나이트
## 8x8 크기의 체스판에서 나이트가 현재 위치에서 움직일 수 있는 경우의 수를 구하라
## 행 위치는 1~8, 열 위치는 a~h로 표현한다
### 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
### 입력문자는 열과 행으로 이뤄진다 (ex: a1)
#### 나이트가 이동할 수 있는 경우의 수 출력

def solution(p):
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    x, y = (ord(p[0]) - 96), int(p[1])
    count = 0

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        count += 1
    
    return count

p = input()
s = solution(p)
print(s)