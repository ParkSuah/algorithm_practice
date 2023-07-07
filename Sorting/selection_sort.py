# 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i, n in enumerate(arr):
    min_num = n
    min_index = i
    for j in range(i + 1, len(arr)):
        if min_num > arr[j]:
            min_num = arr[j]
            min_index = j
    arr[i] = min_num
    arr[min_index] = n

print(arr)
