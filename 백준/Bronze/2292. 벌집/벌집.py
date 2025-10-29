N = int(input())

result = 1
cur = 1
m = 1
while (cur < N):
	cur += 6*m
	m += 1
	result += 1

print(result)