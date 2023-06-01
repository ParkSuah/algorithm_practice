def solution(progresses, speeds):
    answer = []
    count_list = []
    while len(progresses) > 0:
        count = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                continue
        if count > 0:
            count_list.append(count)

    return count_list


# 93 이 하루에 1씩 되면 7일 뒤에 완성되고
# 30 이 하루에 30씩 되면 3일 뒤에 완성되고
# 55 가 하루에 5씩 되면 9일 뒤에 완성된다.
# 그러면 완성된 순서대로 큐에 넣어 놨다가 첫번째 게 다 되면 다 된 애들을 리턴
# 앞에 있는 모든 기능이 완성 안되면 배포가 안됨
# 즉 progresses 안에 들어있는 배열은 큐로 생각되어야 함
# 안에 들어있는 첫번째 수가 100일 때 나올 수 있다.
