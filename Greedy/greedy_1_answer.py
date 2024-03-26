## ver 1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m ==0:   
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second    # 두 번째로 큰 수를 한번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)


## ver 2
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]   # 가장 큰 수
# second = data[n-2]  # 두 번째로 큰 수

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second