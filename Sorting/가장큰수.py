# 정답을 봐버려서 풀 수 없게 된 안좋은 예시


def solution(numbers):
    answer = ""
    biggest = 0
    answer_list = []
    same_dict = {}
    num_list = list(map(str, numbers))
    num_list.sort(key=lambda x: (x * 4)[:4], reverse=True)

    for n in num_list:
        answer += n

    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
