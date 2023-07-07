"""
N명의 모험가가 모험을 떠나고, 각 모험가는 X의 공포도를 가지고 있다. 
X의 공포도를 가진 모험가는 그룹의 인원이 X명 이상이어야만 모험을 떠날 수 있다. 
이 때 모인 사람으로 최대한의 그룹을 만들면 몇 그룹 만들 수 있는지 구하세요. 
단, 모든 사람이 모험을 떠나지 않아도 된다. 
"""


def solution(x_list):
    x_list.sort()
    # [1, 2, 2, 2, 3]
    group_count = 0
    # group = {}
    scary = 1
    # for idx, x in enumerate(x_list):
    #     ...
    while len(x_list) > 0:
        for idx, x in enumerate(x_list):
            print(f"x_list: {x_list}, x: {x}, scary: {scary}")
            group = []
            if x >= scary:
                group.extend(x_list[: idx + 1])
                x_list = x_list[idx + 1 :]
                print(f"group: {group}, left: {x_list}\n")
            # print(f"group_size: {len(group)}")

            if len(group) >= x:
                group_count += 1
                # print(group, x_list)
                break
    print(f"group_count: {group_count}\n==========================")
    return group_count


assert solution([2, 3, 1, 2, 2]) == 2, "Fail"
assert solution([5]) == 0, "Fail"
assert solution([1, 1, 1, 1, 1]) == 5, "Fail"
assert solution([4, 4, 4, 4, 4]) == 1, "Fail"
assert solution([1, 2, 4, 3, 1]) == 2, "Fail"
