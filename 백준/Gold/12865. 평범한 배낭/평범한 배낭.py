N, K = map(int,input().split())
infos = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
	nW = infos[i-1][0]
	nV = infos[i-1][1]
	for j in range(1,K+1):
		dp[i][j] = dp[i-1][j]
		if j-nW >= 0:
			dp[i][j] = max(dp[i][j], dp[i-1][j-nW]+nV)

print(dp[N][K])