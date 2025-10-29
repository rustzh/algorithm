T = int(input())

for test_case in range(T):
	N = int(input())

	clothes = {}
	for i in range(N):
		clothing, clothingType = input().split()
		clothes[clothingType] = clothes.get(clothingType, 0) + 1

	if len(clothes) == 1:
		for value in clothes.values():
			print(value)
	else:
		result = 1
		for value in clothes.values():
			result *= (value+1)
		print(result-1)