import sys
sys.setrecursionlimit(10**7)

n = int(input())
fact = [-1] * (n+1)
fact[0] = 1

def factorial(n):
	if fact[n]!=-1:
		return fact[n]

	fact[n] = n * factorial(n-1)
	return fact[n]

cnt = 0
for k in range(n//2 + 1):
	cnt += factorial(k+n-2*k) // (factorial(k) * factorial(n-2*k))

print(cnt%10007)