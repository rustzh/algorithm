N = int(input())
A = list(map(int,input().split()))

dp = [-1 for i in range(N)]
dp[0] = 1

for i in range(1, N):
	best = 0
	for j in range(0, i+1):
		if A[i] > A[j]:
			best = max(dp[j], best)
	dp[i] = best+1

print(max(dp))