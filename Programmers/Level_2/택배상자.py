# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    answer = 0
    
    container = deque(range(1, len(order) + 1))
    sub_container = deque()
    
    i = 0
    while container or sub_container:
        if container and container[0] == order[i]:
            container.popleft()
            i += 1
            answer += 1
        elif sub_container and sub_container[-1] == order[i]:
            sub_container.pop()
            i += 1
            answer += 1
        else:
            if container:
                box = container.popleft()
                sub_container.append(box)
            else:
                break
    
    return answer

## 문제 해석
# 컨테이너 벨트에는 [1, 2, 3, ..., n]의 택배 상자가 담겨있으며
# 꺼내기만 가능하고 다시 싣는 것은 안된다
# 보조 컨테이너 벨트는 싣고 내리고가 모두 가능하며 선입후출(스택)의 구조를 갖는다