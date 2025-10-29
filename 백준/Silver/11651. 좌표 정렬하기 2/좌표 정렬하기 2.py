import sys

N = int(sys.stdin.readline().rstrip())
points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

points.sort(key=lambda x : (x[1], x[0]))

for point in points:
	print(point[0], point[1])