import sys
n = int(sys.stdin.readline())

dp = [e for e in range(n+1)]

for i in range(n+1):
    if i<2:
        continue
    dp[i] = dp[i-1]+1
    if i>=2:
        dp[i] = min(dp[i-2]+1, dp[i])
    if i>=5:
        dp[i] = min(dp[i-5]+1, dp[i])
    if i>=7:
        dp[i] = min(dp[i-7]+1, dp[i])
        
print(dp[n])