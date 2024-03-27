# 게임 개발
## N, M 크기의 맵이 존재하며 각각의 칸은 육지나 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다
## 각 칸은 (A, B)로 나타내며, A는 북쪽으로부터, B는 서쪽으로부터 떨어진 칸의 개수이다 (좌측 아래 0, 0)
## 1. 왼쪽 방향부터 차례대로 갈 곳을 정함
## 2. 왼쪽에 가보지 않은 칸 존재 = 회전 및 이동, 가보지 않은 칸 없음 = 회전만
## 3. 4방향 모두 가본 칸이거나 바다 = 방향 유지 및 한칸 뒤로, 뒤가 바다일 경우 = 정지
### 첫째 줄에 세로 크기 N, 가로 크기 M을 공백으로 구분하여 입력 (3<= N,M <=50)
### 둘째 줄에 게임 캐릭터가 있는 좌표 (A, B)와 바라보는 방향 d가 서로 공백으로 구분되어 주어진다.
### 방향 d의 값으로는 4가지가 존재한다. (0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽)
### 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. (0: 육지, 1: 바다) 맵의 외곽은 항상 바다
### 처음 캐릭터의 위치는 반드시 육지이다
#### 이동을 마친 후 캐릭터가 방문한 칸의 수 출력

def solution(n, m, charactor, maps):
    count = 1
    check = [[0] * m for _ in range(n)]
    dx = [0, 1, 0, -1] # 북동남서
    dy = [1, 0, -1, 0]
    x, y, d = charactor[0], charactor[1], charactor[2]
    check[x][y] = 1

    turn = 0
    while True:
        # 현재 방향 기준 왼쪽으로 회전
        d -= 1
        if d < 0:
            d = 3
        # 안 가본 곳이면 전진
        nx = x + dx[d]
        ny = y + dy[d]
        if check[nx][ny] == 0 and maps[nx][ny] == 0:
            x, y = nx, ny
            check[x][y] = 1
            count += 1
            turn = 0
            continue
        # 가본 곳이면 일단 정지, 4방향 모두 가본 곳인지 확인 후 후진 및 종료
        else:
            turn += 1
        if turn == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            
            if maps[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
            turn = 0
    return count

n, m = map(int, input().split())
charactor = list(map(int, input().split()))
maps = list()
for i in range(n):
    maps.append(list(map(int, input().split())))

s = solution(n, m, charactor, maps)
print(s)