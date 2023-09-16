def solution(targets):
    answer = 0
    # 타겟의 목표점을 기준으로 정렬
    targets.sort(key=lambda x:x[1])
    print(targets)

    ym = 0 # 요격 미사일 (0,1) 의미
    ym_list = []
    for idx, target in enumerate(targets):
        print(idx, target)
        if idx == 0:
            ym = target[1] - 1
            ym_list.append(ym)
        else:
            if ym >= target[0]:
                continue
            else:
                ym = target[1] - 1
                ym_list.append(ym)
        # if ym not in ym_list:
        #     ym_list.append(ym)

    answer = len(ym_list)
    print(ym_list)
    print(answer)

    return answer


answer = solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
assert answer == 3, "틀렸습니다. 메롱. ㅋ"

print("정답 ~")