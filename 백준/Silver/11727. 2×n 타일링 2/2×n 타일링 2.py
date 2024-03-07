num = int(input())
result = [0, 1, 3]
for i in range(num-2):
    n = i + 3
    result.append(result[n-1] + 2*result[n-2])

print(result[num] % 10007)