# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    def conv(n, k):
        digit = ''
        while n > 0:
            n, mod = divmod(n, k)
            digit += str(mod)
        return digit[::-1]
    
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    numbers = list(map(int, filter(lambda x:x != '', conv(n, k).split('0'))))
    count = 0
    for num in numbers:
        if isPrime(num):
            count += 1
    
    return count