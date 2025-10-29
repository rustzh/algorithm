n, b, a = map(int, input().split())
price = [0] + sorted(list(map(int,input().split())))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
	if i-a <= 0:
		dp[i] = dp[i-1] + price[i]//2
	else:
		dp[i] = dp[i-1] + price[i]//2 + price[i-a]//2


ans = 0
for i in range(n+1):
	if dp[i] <= b:
		ans = i

print(ans)