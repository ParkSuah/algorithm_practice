def solution(priorities, location):
    import time

    answer = 0
    # make item list ~!
    item_q = [i for i in range(len(priorities))]
    doing = []
    sorted = priorities.copy()
    sorted.sort(reverse=True)
    while location in item_q:
        now_item = item_q.pop(0)
        now_prior = priorities.pop(0)
        if now_prior == sorted[0]:
            doing.append(now_item)
            sorted.pop(0)
        else:
            item_q.append(now_item)
            priorities.append(now_prior)

    answer = doing.index(location) + 1
    return answer
