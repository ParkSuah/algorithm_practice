def solution(numbers, target):
    answer = 0
    result = [[numbers[0], 0], [-numbers[0], 0]]  # calc_result, numbers_index

    while result:
        num, idx = result.pop()
        if idx == len(numbers) - 1:
            if num == target:
                answer += 1
        else:
            idx += 1
            result.append([num + numbers[idx], idx])
            result.append([num - numbers[idx], idx])

    return answer
