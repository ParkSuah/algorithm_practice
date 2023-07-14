def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    cnt_boat = 0
    while True:
        if not people:
            break
        person = people[0]
        print(people)
        print(f"now: {person}")
        people.pop(0)
        if limit == person:
            print(person, cnt_boat)
            cnt_boat += 1
            print(f"case1: {person}, {cnt_boat}")
            continue
        else:
            two_flag = False
            for m in people:
                if person + m <= limit:
                    cnt_boat += 1
                    people.remove(m)
                    print(f"case2: {person}, {m}, {cnt_boat}")
                    two_flag = True
                    break
            if not two_flag:
                cnt_boat += 1
                print(f"case3: {person}, {cnt_boat}")

    answer = cnt_boat
    print(cnt_boat)
    return answer


solution([70, 50, 80, 50], 100)
