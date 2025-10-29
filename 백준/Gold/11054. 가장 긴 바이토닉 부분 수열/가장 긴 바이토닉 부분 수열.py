N = int(input())
A = list(map(int, input().split()))

dp = [[-1,-1] for _ in range(N)]
dp[0][0] = 1
dp[-1][1] = 1

for n in range(1, N):
	best = 0
	for a in range(0, n):
		if A[a] < A[n]:
			best = max(dp[a][0], best)
	dp[n][0] = best+1

for n in range(N-2, -1, -1):
	best = 0
	for a in range(N-1, n, -1):
		if A[n] > A[a]:
			best = max(dp[a][1], best)
	dp[n][1] = best+1

result = 0
for i in range(N):
	s = dp[i][0] + dp[i][1]
	result = max(s-1, result)

print(result)