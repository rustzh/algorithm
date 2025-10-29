import sys

lst = []
lines = sys.stdin.readlines()
for line in lines:
    A, B, C = sorted(map(int, line.split()))
    lst.append((A, B, C))

for tri in lst:
	A = tri[0]
	B = tri[1]
	C = tri[2]

	if (A == 0):
		continue
	elif (pow(A,2)+pow(B,2) == pow(C,2)):
		print("right")
	else:
		print("wrong")    