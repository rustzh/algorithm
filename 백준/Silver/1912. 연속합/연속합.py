import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0,0] for _ in range(n)]
dp[0] = [arr[0], -1001]
for i in range(1, n):
	# i가 포함된 최댓값
	dp[i][0] = max(arr[i], dp[i-1][0]+arr[i])
	# i가 포함되지 않은 최댓값
	dp[i][1] = max(dp[i-1])
	
print(max(dp[n-1]))