import sys

N = int(sys.stdin.readline().rstrip())

arr = []
for i in range(N):
	s = sys.stdin.readline().rstrip()
	arr.append(s)

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x : len(x))

for u in arr:
	print(u)