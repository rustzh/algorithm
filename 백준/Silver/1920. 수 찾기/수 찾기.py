N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

def binary_search(num):
	left = 0
	right = len(A)-1

	while (left <= right):
		mid = (left+right)//2

		if A[mid] < num:
			left = mid+1
		if A[mid] > num:
			right = mid-1
		if A[mid] == num:
			return 1
	return 0

for x in B:
	print(binary_search(x))
