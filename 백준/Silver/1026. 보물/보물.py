n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_complete = [False for _ in range(n)]
b_complete = [False for _ in range(n)]

S = 0
for i in range(n):
	max_b = 0
	for j in range(n):
		if max_b <= b[j] and b_complete[j]==False:
			max_b = b[j]
			idx_max_b = j

	min_a = 100
	for j in range(n):
		if min_a >= a[j] and a_complete[j]==False:
			min_a = a[j]
			idx_min_a = j

	b_complete[idx_max_b] = True
	a_complete[idx_min_a] = True
	S += max_b * min_a

print(S)