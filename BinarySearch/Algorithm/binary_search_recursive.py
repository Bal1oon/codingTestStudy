def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
target = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, len(array) - 1)
print(target)
print(array)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)