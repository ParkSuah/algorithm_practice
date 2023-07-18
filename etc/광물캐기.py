def solution(picks, minerals):
    answer = 0
    mineral_idx = 0
    pick_idx = 0  # 다이아 곡괭이로 시작
    pick_power = {0: [1, 1, 1], 1: [5, 1, 1], 2: [25, 5, 1]}
    for p in picks:
        left = p
        count = 0
        if p == 0:
            continue
        while left > 0 and len(minerals) > mineral_idx:
            print(mineral_idx)
            if minerals[mineral_idx] == "diamond":
                answer += pick_power[pick_idx][0]
            elif minerals[mineral_idx] == "iron":
                answer += pick_power[pick_idx][1]
            else:
                answer += pick_power[pick_idx][2]
            count += 1
            if count == 5:
                count = 0
                left -= 1
                pick_idx += 1
            print(
                f"곡괭이 종류: {mineral_idx}, count: {count}, mineral_idx: {mineral_idx}, 광물: {minerals[mineral_idx]}, 피로도: {answer}"
            )
            mineral_idx += 1

    return answer


# solution(
#     [1, 3, 2],
#     ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
# )

solution(
    [0, 1, 1],
    [
        "diamond",
        "diamond",
        "diamond",
        "diamond",
        "diamond",
        "iron",
        "iron",
        "iron",
        "iron",
        "iron",
        "diamond",
    ],
)
