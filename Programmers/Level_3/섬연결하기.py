# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x: x[2])
    
    for i, j, cost in costs:
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
            answer += cost    
    
    return answer