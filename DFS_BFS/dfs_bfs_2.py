# 미로 탈출
## N x M 크기의 미로가 있을 때, 괴물이 있는 부분에는 0, 괴물이 없는 부분에는 1로 표시되어있다.
## 현재 위치는 (1, 1)이며, 출구는 (N, M)일 때 탈출하기 위한 최소 칸의 개수를 구하라 (시작 칸과 마지막 칸을 모두 포함한다).
### 첫째 줄에 N, M이 주어진다
### 둘째 줄부터 미로의 정보가 0, 1로 주어진다. 각각의 수는 공백 없이 주어지며, 시작, 마지막칸은 항상 1이다
#### 최소 이동 칸의 개수 출력

from collections import deque

def solution(n, m, maze):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maze[nx][ny] == 0:
                    continue
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny))
    
    bfs(0, 0)
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [ list(map(int, input())) for _ in range(n) ]

s = solution(n, m, maze)
print(s)