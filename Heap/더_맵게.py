import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    if len(scoville) == 1:
        if scoville[0] < K:
            answer = -1
        return answer

    while scoville[0] < K:
        hottest = heapq.heappop(scoville)
        hotter = heapq.heappop(scoville)
        new_hot = hottest + (hotter * 2)
        heapq.heappush(scoville, new_hot)
        answer += 1
        if len(scoville) <= 1:
            break
        # print(answer)
    if scoville[0] < K:
        answer = -1
    # print(answer)
    return answer
