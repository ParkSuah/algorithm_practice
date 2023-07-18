# 광산에 있는 모든 광물을 캐거나
# 더 이상 곡괭이가 없을 때까지 광물을 캔다. . .
# 광물보다 곡괭이가 많이 남았을 경우, 어떤 곡괭이를 선택해도 된다. 

def solution(picks, minerals):
    answer = 0
    mineral_idx = 0
    pick_idx = 0  # 다이아 곡괭이로 시작
    pick_dict = {
        0: '다이아몬드', 
        1: '철', 
        2: '돌'
    }
    pick_power = {0: [1, 1, 1], 1: [5, 1, 1], 2: [25, 5, 1]}
    for p in picks:
        left = p # 특정 종류의 곡괭이가 남은 갯수
        count = 0
        if p == 0:
            print(f"{pick_dict[pick_idx]} 곡괭이는 0개입니다.")
            pick_idx += 1
            continue
        while left > 0 and len(minerals) > mineral_idx:
            if minerals[mineral_idx] == "diamond":
                answer += pick_power[pick_idx][0]
            elif minerals[mineral_idx] == "iron":
                answer += pick_power[pick_idx][1]
            else:
                answer += pick_power[pick_idx][2]
            count += 1 # 이 곡괭이를 몇번 사용했는지 카운트
            print(
                f"곡괭이 종류: {pick_dict[pick_idx]}, count: {count}, mineral_idx: {mineral_idx}, 광물: {minerals[mineral_idx]}, 피로도: {answer}"
            )
            if count == 5:
                count = 0
                left -= 1
                pick_idx += 1
            mineral_idx += 1

    return answer


# solution(
#     [1, 3, 2],
#     ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
# )

# solution(
#     [0, 1, 1],
#     [
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#     ],
# )

solution(
    [1, 0, 1], ["iron", "iron", "iron", "iron", "diamond", "diamond", "diamond"]
)