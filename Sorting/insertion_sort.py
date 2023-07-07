# 카드를 넣을 수 있는 곳을 찾은 후에 넣는다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

sorted_list = []

for i in range(len(arr)):
    if i == 0:
        sorted_list.append(arr[i])
    else:
        insert_flag = False
        for idx, j in enumerate(sorted_list):
            if arr[i] < j:
                smaller_list = sorted_list[:idx]
                bigger_list = sorted_list[idx:]
                sorted_list = smaller_list + [arr[i]] + bigger_list
                insert_flag = True
                break
        if not insert_flag:
            sorted_list.append(arr[i])
print(sorted_list)
