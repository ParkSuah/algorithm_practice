# 당장의 두자리 수를 비교해서 작은걸 앞으로, 큰걸 뒤로 보내도록 자리를 바꾼다.
# 더 이상 정렬이 필요없을 때까지 반복

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
while True:
    count = 0
    for i in range(len(arr) - 1):
        a = arr[i]
        b = arr[i + 1]
        if a > b:
            arr[i] = b
            arr[i + 1] = a
            count += 1
        print(arr)
    if count == 0:
        break
