n = int(input())
arr = [0 for _ in range(n+1)]

def fibo(n):
	if n == 0:
		return arr[n]
	if n == 1:
		arr[1] = 1
		return arr[n]
	arr[n] = fibo(n-1) + fibo(n-2)
	return arr[n]

print(fibo(n))