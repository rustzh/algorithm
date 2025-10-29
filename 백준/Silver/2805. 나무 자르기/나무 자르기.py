# 높이가 k일 때 가능한가?

def is_possible(k):
	global N, M, heights

	cnt = 0
	for h in heights:
		if h > k:
			cnt += (h-k)

	return (cnt >= M)

N, M = map(int,input().split())
heights = list(map(int, input().split()))

result = -1

left = 0
right = int(1e9)

while left <= right:
	mid = (left + right) // 2

	if is_possible(mid):
		left = mid+1
		result = mid
	else:
		right = mid-1

print(result)