K, N = map(int, input().split())

lines = []
for i in range(K):
	lines.append(int(input()))

# 최소 1,  최대 랜선 중 가장 긴 길이
# 중간 값에서, mid 길이로 각 랜선에서 몇 개의 랜선이 가능한지 계싼

left = 1
right = max(lines)

result = 0
while (left <= right):
	mid = (left+right)//2

	cnt = 0
	for line in lines:
		cnt += (line//mid)

	if N <= cnt:
		result = mid
		left = mid+1
	else:
		right = mid-1

print(result)