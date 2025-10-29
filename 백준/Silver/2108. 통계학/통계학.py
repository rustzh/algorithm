import sys
import math

N = int(sys.stdin.readline().rstrip())
nums = []
for i in range(N):
	nums.append(int(sys.stdin.readline().rstrip()))

print(math.floor((sum(nums)/N) + 0.5))

nums.sort()
print(nums[N//2])

num_counts = {}
for i in range(N):
	num_counts[nums[i]] = num_counts.get(nums[i], 0) +1
max_value = max(num_counts.values())
max_nums = [num for num, count in num_counts.items() if count == max_value]
if len(max_nums) > 1:
	print(max_nums[1])
else:
	print(max_nums[0])

print(max(nums) - min(nums))