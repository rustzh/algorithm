N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(N, 1, -1):
	if i%3 == 0:
		if dp[i//3] == 0:
			dp[i//3] = dp[i]+1
		else:
			dp[i//3] = min(dp[i//3], dp[i]+1)

	if i%2 == 0:
		if dp[i//2] == 0:
			dp[i//2] = dp[i]+1
		else:
			dp[i//2] = min(dp[i//2], dp[i]+1)

	if dp[i-1] == 0:
		dp[i-1] = dp[i] + 1
	else:
		dp[i-1] = min(dp[i-1], dp[i]+1)

print(dp[1])