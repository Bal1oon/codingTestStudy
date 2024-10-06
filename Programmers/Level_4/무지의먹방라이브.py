def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times = [(t, i) for i, t in enumerate(food_times)]
    food_times.sort()

    previous = 0
    for i in range(len(food_times)):
        diff = food_times[i][0] - previous
        if diff != 0:
            spend = diff * (len(food_times) - i)
            if spend <= k:
                k -= spend
                previous = food_times[i][0]
            else:
                k %= (len(food_times) - i)
                food_times = sorted(food_times[i:], key=lambda x: x[1])
                return food_times[k][1] + 1

    return -1