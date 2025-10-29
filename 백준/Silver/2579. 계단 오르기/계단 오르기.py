N = int(input())
scores = [int(input()) for _ in range(N)]
dp = [[0, 0]]*N # [이전에 1칸, 이전에 2칸] 일 때의 최대값
dp[0] = [scores[0], scores[0]]

if N > 1:
	dp[1] = [scores[0]+scores[1], scores[1]]
	for i in range(2, N):
		dp[i] = [dp[i-1][1]+scores[i], max(dp[i-2])+scores[i]]

print(max(dp[N-1]))