# 떡볶이 떡 만들기
## 길이가 일정하지 않은 떡을 높이(H)로 지정한 절단기로 절단한다.
## 손님이 요청한 총 길이가 M일 때 적오도 M만큼의 떡을 얻기 위한 절달기 높이의 최댓값을 구하라
### 1. 떡 개수 N, 필요한 떡의 길이 M
### 2. N개의 떡의 개별 높이
#### 적어도 M만큼의 떡을 가져가기 위한 절단기 설정 최대 높이를 출력

def solution(m, cakes):
    start = 0
    end = max(cakes)

    result = 0
    while start <= end:
        sum_ = 0
        mid = (start + end) // 2
        for cake in cakes:
            if cake > mid:
                sum_ += cake - mid
        if sum_ < m:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    return result

n, m = map(int, input().split())
cakes = list(map(int, input().split()))

s = solution(m, cakes)
print(s)