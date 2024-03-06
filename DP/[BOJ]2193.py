num = int(input())
    
# result = [[0] * 2 for _ in range(num)]
result = [[0, 1]]
    
for i in range(num):
    n = i+1
    result.append([result[n-1][0]+result[n-1][1], result[n-1][0]])
    
print(sum(result[num-1]))