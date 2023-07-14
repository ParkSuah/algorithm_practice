def solution(people, limit):
    answer = 0
    index = 0
    length = len(people) - 1
    people.sort(reverse=True)
    while True:
        person = people[index]
        print(people)
        print(f"now: {person}")
        index += 1  # people.pop(0)
        if limit == person:
            print(person, answer)
            answer += 1
            print(f"==> case1: {person}, {answer}")
            continue
        else:
            if len(people) > 0:
                print(people, people[-1] + person)
                if people[-1] + person <= limit:
                    answer += 1
                    index += 1  # p = people.pop()
                    print(f"==> case2: {person}, {people[-1]}, {answer}")
                    continue
            answer += 1
            print(f"==> case3: {person}, {answer}")
        if length - 1 == index:
            break
    print(answer)
    return answer


solution([70, 50, 80, 50], 100)
print("=============================")
solution([70, 80, 50], 100)
