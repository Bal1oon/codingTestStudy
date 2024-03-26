# 큰 수의 법칙
## 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 횟수 제한 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오
### 첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다. (K는 M보다 작거나 같다)
### 둘째 줄에 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#### 큰 수의 법칙에 따라 더해진 값 출력

def solution(n, m, k, nums):
    result = 0
    nums.sort(reverse = True)

    result += nums[0] * (m//k) * k
    result += nums[1] * (m%k)
    
    return result

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

s = solution(n, m, k, nums)
print(s)