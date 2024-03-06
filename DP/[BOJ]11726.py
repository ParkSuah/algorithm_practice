num = int(input())
result = [1, 2]
for i in range(num-2):
    # n = i+2
    result.append((result[i] + result[i+1])%10007)
print(result[num-1])