import math
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
	n = int(input())
	result = 0

	a = int(math.log(n, 5))

	for i in range(1, a+1):
		b = pow(5,i)
		result += int(n/b)

	print(result)