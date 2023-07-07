arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 재귀로 작성해보자
import time


result = []


def quicksort(arr):
    if len(arr) <= 1:
        print(f"len 1 return : {arr}")
        return arr

    pivot = arr[0]
    print(pivot)
    bigger_list = []
    smaller_list = []
    equal_list = []
    for i in range(len(arr)):
        if arr[i] > pivot:
            bigger_list.append(arr[i])
        elif arr[i] < pivot:
            smaller_list.append(arr[i])
        else:
            equal_list.append(arr[i])

    time.sleep(3)
    print(bigger_list)
    print(smaller_list)
    return quicksort(smaller_list) + equal_list + quicksort(bigger_list)


print(quicksort(arr))
