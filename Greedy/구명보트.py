def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    cnt_boat = 0
    while True:
        if not people:
            break
        cnt_person = 0
        sum_weight = 0
        idx = 0
        # if sum_weight < limit:
        for idx, p in enumerate(people):
            sum_weight += p
            if sum_weight <= limit:
                cnt_boat += 1
                cnt_person += 1
                print(cnt_boat, people[idx])
                people.pop(idx)
                if cnt_person == 2:
                    cnt_person = 0
                    idx = 0
                    break
            else:
                cnt_boat += 1
                print(cnt_boat, people[idx])
                people.pop(idx)
                idx = 0
                break

    answer = cnt_boat
    print(cnt_boat)
    return answer


solution([70, 50, 80, 50], 100)
