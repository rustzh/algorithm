def solve(arr):
	for i in range(8):
		if arr[i] == i+1:
			if i == 7:
				print("ascending")
				return
			continue
		break
	
	for i in range(8):
		if arr[i] == 8-i:
			if i == 7:
				print("descending")
				return
			continue
		break
	
	print("mixed")
	return
		

arr = list(map(int, input().split()))

solve(arr)