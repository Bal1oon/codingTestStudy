# 음료수 얼려 먹기
## N x M 크기의 얼음 틀이 있을 때, 구멍 뚫린 곳은 0, 칸막이가 존재하는 부분은 1로 표시된다.
## 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우, 서로 연결되어 있는 것으로 간주한다.
## 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라
### 첫 번째 줄에 세로 길이 N, 가로 길이 M이 주어진다.
### 두 번째 줄부터 N+1 번째 줄까지 틀의 형태가 주어진다.
#### 한 번에 만들 수 있는 아이스크림의 개수 출력

def solution(n, m, graph):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x-1, y)
            dfs(x+1, y)
            return True
        return False

    count = 0    
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1
    return count


    

n, m = map(int, input().split())
frame = []
for _ in range(n):
    frame.append(list(map(int, input())))
    
s = solution(n, m, frame)
print(s)