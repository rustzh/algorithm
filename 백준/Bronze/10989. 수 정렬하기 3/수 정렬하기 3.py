import sys

N = int(sys.stdin.readline())

count = [0]*10001

for i in range(N):
	n = int(sys.stdin.readline())
	count[n] += 1

for i in range(1, 10001):
	for j in range(count[i]):
		print(i)