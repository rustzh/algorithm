import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = {}
names = {}

for i in range(1, N+1):
	poketmon = sys.stdin.readline().rstrip()
	numbers[i] = poketmon
	names[poketmon] = i

for i in range(M):
	q = sys.stdin.readline().rstrip()

	if q.isdigit():
		print(numbers.get(int(q)))

	else:
		print(names.get(q))