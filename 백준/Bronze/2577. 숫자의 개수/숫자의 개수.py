A = int(input())
B = int(input())
C = int(input())

arr = [0 for _ in range(10)]

num = str(A*B*C)
for i in range(len(num)):
	arr[int(num[i])] += 1
	
for i in range(10):
	print(arr[i])