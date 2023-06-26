from itertools import *


def solution(clothes):
    answer = 0

    clothes_set = {}
    for each in clothes:
        if each[1] not in clothes_set:
            clothes_set[each[1]] = [each[0]]
        else:
            clothes_set[each[1]].append(each[0])

    # 모든 옷 종류 조합을 구함 key값으로
    set_list = []
    for i in range(len(clothes_set.keys())):
        set_list.append(list(combinations(clothes_set.keys(), i + 1)))
    # print(set_list)

    for each_set in set_list:
        # print(each_set)
        for i in range(len(each_set)):
            each_sum = 1
            for codi in each_set[i]:
                each_sum *= len(clothes_set[codi])
            answer += each_sum
    return answer


# 30갸지의 다른 옷이 한개씩 있는 경우 시간초과됨

if __name__ == "__main__":
    clothes = [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"],
    ]
    correct_answer = 5
    assert solution(clothes) == correct_answer

    clothes = [
        ["1"],
        ["2"],
        ["3"],
        ["4"],
        ["5"],
        ["6"],
        ["7"],
        ["8"],
        ["9"],
        ["10"],
        ["11"],
        ["12"],
        ["13"],
        ["14"],
        ["15"],
        ["16"],
        ["17"],
        ["18"],
        ["19"],
        ["20"],
        ["21"],
        ["22"],
        ["23"],
        ["24"],
        ["25"],
        ["26"],
        ["27"],
        ["28"],
        ["29"],
        ["30"],
    ]
    correct_answer = 1073741823
    # assert solution(clothes) == correct_answer
