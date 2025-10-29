import sys

def kanto(n):
	if (n==0): return '-'
	return kanto(n-1) + (3**(n-1))*' ' + kanto(n-1)

lines = sys.stdin.readlines()
for line in lines:
	n = int(line)
	
	print(kanto(n))