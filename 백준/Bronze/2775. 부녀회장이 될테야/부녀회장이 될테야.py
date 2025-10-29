apt = [[0]*15 for _ in range(15)]

for i in range(1,15):
	apt[0][i] = i

for a in range(1, 15):
	apt[a][1] = 1
	for b in range(1, 15):
		apt[a][b] = apt[a-1][b] + apt[a][b-1]

T = int(input())

for i in range(T):
	k = int(input())
	n = int(input())

	print(apt[k][n])