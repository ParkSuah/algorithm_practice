def long_int(n):
    result = ''
    byte_amount = n/4

    if byte_amount%1.0 > 0:
        byte_amount = int(n/4) + 1
    for i in range(int(byte_amount)):
        result += 'long '
# n 은 항상 4의 배수라는 조건이 있으니까 딱히 나머지 경우를 신경 안 써도 됨 ..
    result += 'int'
    print(result)

if __name__ == '__main__':
    long_int(9)
    long_int(4)
    long_int(20)
    long_int(8)
