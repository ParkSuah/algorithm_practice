# 교훈: 문제를 ... 자세히 읽어보자 ^^;

from itertools import product


def solution(users, emoticons):
    # emoticons.sort()
    answer = []
    # 할인율에 따른 이모티콘 가격
    pricing_list = []
    for e in emoticons:
        pricing_list.append([10, 20, 30, 40])
    product_price = list(product(*pricing_list))
    # print(product_price)
    most_reg = 0
    most_price = 0
    # most_list = []
    # product_price = [(40, 40, 20, 40)]
    for pp in product_price:
        emoticon_plus = 0
        price_sum = 0
        # print(pp)
        for u in users:
            paid = 0
            for p, e in zip(pp, emoticons):
                if p >= u[0]:
                    paid += int((100 - p) * 0.01 * e)
            if paid >= u[1]:
                emoticon_plus += 1
                # print(f"user: {u}, emoticon_plus: {emoticon_plus}, paid: {paid}")
            else:
                price_sum += paid
                # print(f"user: {u}, price_sum: {price_sum}, paid: {paid}")
        if most_reg == emoticon_plus:
            print(f"{most_reg} == {emoticon_plus}")
            print(f"이모티콘 할인율: {pp}, price_sum: {price_sum}")
            if most_price < price_sum:
                most_price = price_sum
                most_list = pp
                # print(most_reg, most_price, most_list)
        elif most_reg < emoticon_plus:
            most_reg = emoticon_plus
            most_price = price_sum
            most_list = pp
            # print(most_reg, most_price, most_list)

    print(f"most_reg: {most_reg}, most_price: {most_price}")
    return answer


# solution([[40, 10000], [25, 10000]], [7000, 9000])
solution(
    [
        [40, 2900],
        [23, 10000],
        [11, 5200],
        [5, 5900],
        [40, 3100],
        [27, 9200],
        [32, 6900],
    ],
    [1300, 1500, 1600, 4900],
)
