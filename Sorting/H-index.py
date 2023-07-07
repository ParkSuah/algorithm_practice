def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    # print(citations)
    for idx, c in enumerate(citations):
        h = idx + 1  # h 번 이상 인용된 논문의 개수
        if h >= c:
            print("h >= c")
            answer = c
            print(f"{c}번 이상 인용된 논문이 {h}개")
            continue
        if h < c:
            print("c > h")
            answer = h + 1
            print(f"{c}번 이상 인용된 논문이 {h}개")
    # print(answer)
    return answer


def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)  # 논문 개수
    h = 0
    h_count = 0
    while h <= h_count:
        h += 1
        for i, c in enumerate(citations):
            if c >= h:
                h_count = n - i  # len(citations[i:])
                print(h, citations[i:])
                break

    answer = h - 1

    print(answer)

    return answer


solution([6, 6, 6, 6, 6, 1])
