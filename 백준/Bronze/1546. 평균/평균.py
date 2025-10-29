import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().strip().split()))

M = max(scores)

for i in range(N):
	scores[i] = scores[i]/M*100

result = sum(scores)/N

print(result)