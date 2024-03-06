cnt = int(input())

for num in range(cnt):
    n = int(input())
    s = []
    s.append(list(map(int, input().split())))
    s.append(list(map(int, input().split())))
    
    max_dp = [[0 for _ in range(n)]for _ in range(2)] # max_dp[a][b] = a행 b열의 스티커를 마지막으로 선택할 때 max sum 저장
    
    if n == 1:
        max_dp[0][0] = s[0][0]
        max_dp[1][0] = s[1][0]
    if n == 2:
        max_dp[0][1] = s[1][0]+s[0][1]
        max_dp[1][1] = s[0][0]+s[1][1]
    
    max_dp[0][0] = s[0][0]
    max_dp[1][0] = s[1][0]
    if n == 1:
        print(max(max_dp[0][0], max_dp[1][0]))
        continue
    max_dp[0][1] = s[1][0]+s[0][1]
    max_dp[1][1] = s[0][0]+s[1][1]
    if n == 2:
        print(max(max_dp[0][1], max_dp[1][1]))
        continue
    for i in range(n-2):
        max_dp[0][i+2] = max(max_dp[1][i+1]+s[0][i+2], max_dp[0][i]+s[0][i+2], max_dp[1][i]+s[0][i+2])
        max_dp[1][i+2] = max(max_dp[0][i+1]+s[1][i+2], max_dp[0][i]+s[1][i+2], max_dp[1][i]+s[1][i+2])
    
    max_sum = max(max_dp[0][n-1], max_dp[1][n-1])        
    print(max_sum)