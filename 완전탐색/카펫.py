def solution(brown, yellow):
    answer = []
    area = brown + yellow

    edge_list = []
    for i in range(area):
        sero = i + 1
        if area % sero == 0:
            garo = area // sero
            if garo >= sero and sero > 2:
                edge_list.append([garo, sero])
    print(edge_list)

    for each in edge_list:
        yellow_garo = each[0] - 2
        yellow_sero = each[1] - 2
        if 2 * yellow_garo + 2 * yellow_sero + 4 == brown:
            answer = each

    print(answer)
    return answer


solution(24, 24)
