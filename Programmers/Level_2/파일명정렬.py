# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    parts = []
    
    for file in files:
        i = 0
        while i < len(file):
            if file[i].isdigit():
                break
            i += 1
        parts.append([file[:i]])
        j = len(parts[-1][0])
        
        while i < len(file):
            if not file[i].isdigit():
                break
            i += 1
        parts[-1].append(file[j:i])
        parts[-1].append(file[i:])
    
    parts.sort(key = lambda x : (x[0].lower(), int(x[1])))
    file_sorted = [''.join(part) for part in parts]
    
    return file_sorted