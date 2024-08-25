# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])
    d = [-1] * (n+1)
    d[1] = 0
    
    while q:
        cur = q.popleft()
        
        for n in graph[cur]:
            if d[n] == -1:
                d[n] = d[cur] + 1
                q.append(n)
    
    answer = d.count(max(d))
    return answer