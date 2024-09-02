# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0

    while storey > 0:
        storey, last_digit = divmod(storey, 10)

        if last_digit > 5 or (last_digit == 5 and storey % 10 >= 5):
            last_digit = (10 - last_digit)
            storey += 1
        answer += last_digit
    
    return answer

# def solution(storey):
#     answer = 0

#     while storey > 0:
#         last_digit = storey % 10
        
#         if last_digit < 5:
#             answer += last_digit
#         elif last_digit == 5:
#             answer += last_digit
#             if (storey // 10) % 10 >=5:
#                 storey += 10
#         else:
#             answer += (10 - last_digit)
#             storey += 10
        
#         storey //= 10
    
#     return answer