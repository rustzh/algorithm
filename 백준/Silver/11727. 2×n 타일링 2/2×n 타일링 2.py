n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
	if i == 2:
		dp[i] = 3
	else:
		dp[i] = (dp[i-1] + dp[i-2]*2)%10007
	
print(dp[n])