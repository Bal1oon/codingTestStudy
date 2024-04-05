# 문자열 뒤집기
## 0과 1로만 이뤄진 문자열 S가 있고, S에 있는 모든 숫자를 같게하려고 한다.
## 이때, 연속된 하나 이상의 숫자를 모두 뒤집을 수 있다.
## 최소 몇 번의 뒤집기로 모두 같은 숫자로 만들 수 있는지 구하라
### 0과 1로 이뤄진 문자열 S 입력
#### 뒤집는 행동의 최소 횟수 출력

s = input()

count0 = 0
count1 = 0
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))