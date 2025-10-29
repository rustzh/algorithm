choose = []

def combination(index, level):
	if level==6: 
		for u in choose:
			print(u, end=' ')
		print()
		return

	for i in range (index, k):
		choose.append(arr[i])
		combination(i+1, level+1)
		choose.pop()


while True:
	lst = list(map(int, input().split()))

	k = lst[0]
	arr = lst[1:]
	if k==0:
		break

	combination(0,0)
	print()