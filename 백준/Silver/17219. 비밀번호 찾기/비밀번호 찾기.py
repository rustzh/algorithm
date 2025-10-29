import sys

N, M = map(int, sys.stdin.readline().split())
pws = {}

for i in range(N):
	site, pw = sys.stdin.readline().rstrip().split()
	pws[site] = pw

for i in range(M):
	q = sys.stdin.readline().rstrip()
	print(pws[q])