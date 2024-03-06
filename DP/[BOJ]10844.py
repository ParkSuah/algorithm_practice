num = int(input())
result = [[0] * 10 for _ in range(num)] # 0~9
    
for i in range(num):
    for j in range(10):
        n = j
        if i > 0:
            if n == 0:
                result[i][n] = result[i-1][1]
            elif n == 9:
                result[i][n] = result[i-1][8]
            else:
                result[i][n] = result[i-1][n-1] + result[i-1][n+1]
        else:
            if n == 0:
                result[i][n] = 0
            else:
                result[i][n] = 1
print(sum(result[num-1])%1000000000)