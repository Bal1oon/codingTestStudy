# https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    answer = []
    dic = {}
    
    for r in record:
        parts = r.split()
        action, uid = parts[0], parts[1]
        if action in ['Enter', 'Change']:
            dic[uid] = parts[2]
    
    for r in record:
        parts = r.split()
        action, uid = parts[0], parts[1]
        
        if action == 'Enter':
            answer.append(f'{dic[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{dic[uid]}님이 나갔습니다.')
    
    return answer

## record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
## result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]