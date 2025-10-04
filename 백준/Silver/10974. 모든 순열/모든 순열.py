n = int(input())

lst = [i for i in range(1, n+1)]
check = [False for _ in range(n)]
choose = []

def permutation(level):
	if level==n:
		for u in choose:
			print(u, end=' ')
		print('')
		return

	for i in range(0, n):
		if check[i]==True:
			continue

		choose.append(lst[i])
		check[i] = True

		permutation(level+1)

		check[i] = False
		choose.pop()

permutation(0)