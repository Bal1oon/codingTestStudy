# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    cmd = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    cur = (0, 0)
    visited = set()
    
    for move in dirs:
        dx, dy = cmd[move]
        next_x, next_y = cur[0] + dx, cur[1] + dy
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            visited.add( (cur, (next_x, next_y)) )  # 1->2 와 2->1 은 길이 같음으로 모두 추가
            visited.add( ((next_x, next_y), cur) )
            cur = (next_x, next_y)
    
    answer = len(visited) // 2    
    return answer