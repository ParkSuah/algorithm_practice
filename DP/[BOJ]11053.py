cnt = int(input())
num_list = list(map(int, input().split()))
num_list.insert(0, 0)
dp = [0 for _ in range(cnt+1)]
for i in range(1, cnt+1): # 1 ~ cnt-1
    less_dp = []
    for j in range(i): # 0 ~ i
        if num_list[(i-j)-1] < num_list[i]: # 여기서 dp 값도 같이 보는 게 point !!
            less_dp.append(dp[(i-j)-1])
    dp[i] = max(less_dp) + 1
# print(num_list)
# print(dp)
print(max(dp))