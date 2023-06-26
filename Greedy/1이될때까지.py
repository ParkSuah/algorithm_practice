"""
어떠한 수 N이 1이 될때까지 특정 연산을 반복수행함
1. N - 1
2. N / K
두가지 중 하나를 선택해 수행했을 때 가장 적게 수행하면서 N을 1로 만들 수 있는 횟수를 구하세요.
단, 2번은 N이 K로 나누어 떨어질 때만 선택 가능
"""
from time import sleep


def solution(n, k):
    count = 0

    while True:
        if n % k == 0:
            n //= k
            count += 1
            if n == 1:
                return count
        else:
            n -= 1
            count += 1


# 시간복잡도 줄이기
def solution(n, k):
    count = 0

    while True:
        target = n % k
        count += target
        n -= target
        if n % k == 0:
            n //= k
            count += 1
            if n == 1:
                return count
        # else:
        #     n -= 1
        #     count += 1


print(solution(17, 4))
