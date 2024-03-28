# 성적이 낮은 순서로 학생 출력하기
### 1. 학생 수 N 입력
### 2 ~ N+1. 학생의 이름과 성적을 공백으로 구분하여 입력
#### 모든 학생의 이름을 성적이 낮은 순서대로 출력. 성적 동일시 순서 상관 없음

def solution(arr):
    arr = sorted(arr, key = lambda arr: int(arr[1]))
    for student in arr:
        print(student[0], end=' ')

n = int(input())
arr = [input().split() for _ in range(n)]

solution(arr)
