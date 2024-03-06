num = int(input())
a = 0
min_list = [0] # 1의 최소 횟수만 넣어두고 리스트 시작
for i in range(num-1):
    n = i+2
    idx = i+1
    a = min_list[idx-1] + 1
    if n % 3 == 0:
        a = (min_list[n//3 - 1] + 1) if (min_list[n//3 - 1] + 1) < a else a
    if n % 2 == 0:
        a = (min_list[n//2 - 1] + 1) if (min_list[n//2 - 1] + 1) < a else a
        
    min_list.append(a)
    
print(min_list[num-1])