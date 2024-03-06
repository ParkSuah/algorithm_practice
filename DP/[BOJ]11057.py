num = int(input())
    
result = [[0] * 10 for _ in range(num)]
    
for i in range(num):
    for n in range(10):
        if i == 0: # 첫번째 자리표
            result[i][n] = 1
        else:
            for j in range(n+1):
                result[i][n] += result[i-1][j]
                    
print(sum(result[num-1])%10007)