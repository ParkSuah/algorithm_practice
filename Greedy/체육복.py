def solution(n, lost, reserve):
    # 전체 학생 리스트
    student = [False for i in range(n)]

    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))

    for idx, s in enumerate(student):
        p_num = idx + 1
        if p_num in set_lost:
            if p_num - 1 in set_reserve:
                set_reserve.remove(p_num - 1)
                student[p_num - 1] = True
            elif p_num + 1 in set_reserve:
                set_reserve.remove(p_num + 1)
                student[p_num - 1] = True
        else:
            student[p_num - 1] = True
        print(student)

    if False in student:
        student.remove(False)
    answer = len(student)

    return answer


assert solution(5, [1, 2, 3], [2, 3, 4]) == 4, "Fail"
