cnt = int(input())
wine = [0 for _ in range(cnt)]
for i in range(cnt):
    wine[i] = int(input())

dp = [0 for _ in range(cnt+1)] # 규칙성 쉽게 만들려고 dp[0]=0 추가
for i in range(cnt+1):
    if i == 0:
        pass
    elif i == 1:
        dp[i] = wine[0]
    elif i == 2:
        dp[i] = wine[0]+wine[1]
    else:
        dp[i] = max(dp[i-3]+wine[i-2]+wine[i-1], dp[i-2]+wine[i-1], dp[i-1])
print(dp[cnt])