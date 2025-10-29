N, r, c = map(int, input().split())

def solve(n, r, c):
	if n==1:
		if r==0 and c==0:
			return 0
		elif r==0 and c==1:
			return 1
		elif r==1 and c==0:
			return 2
		elif r==1 and c==1:
			return 3

	else:
		tmp = 2**(n-1)

		if r<tmp and c>=tmp:
			extra = 2**((n-1)*2)
		elif r>=tmp and c<tmp:
			extra = 2**((n-1)*2)*2
		elif r>=tmp and c>=tmp:
			extra = 2**((n-1)*2)*3
		else:
			extra = 0

	return solve(n-1, r%tmp, c%tmp) + extra

print(solve(N,r,c))