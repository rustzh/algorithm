import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
psum = [0] * (N+1)

for i in range(1, N+1):
	psum[i] = psum[i-1] + arr[i]

for i in range(M):
	a, b = map(int, sys.stdin.readline().split())
	print(psum[b]-psum[a-1])