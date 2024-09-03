# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math
from collections import defaultdict

def time_to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(fees, records):
    result = []
    
    parking = dict()
    parking_time = defaultdict(int)
    
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    for record in records:
        time, number, status = record.split()
        minutes = time_to_minutes(time)
        
        if status == 'IN':
            parking[number] = minutes
        else:
            in_time = parking.pop(number)
            parking_time[number] += minutes - in_time
    
    end_time = time_to_minutes('23:59')
    for number, in_time in parking.items():
        parking_time[number] += end_time - in_time
        
    for number in sorted(parking_time.keys()):
        time = parking_time[number]
        
        if time <= basic_time:
            result.append(basic_fee)
        else:
            fee = basic_fee + math.ceil( (time - basic_time) / unit_time ) * unit_fee
            result.append(fee)
        
    return result
            