board = [list(map(int,input().split())) for _ in range(9)]

row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
square = [[set() for _ in range(3)] for _ in range(3)]

def search(level):
	global pos, row, col, square

	if level == len(pos):
		for i in range(9):
			for j in range(9):
				print(board[i][j], end=' ')
			print('')
		exit(0)
		return

	x, y = pos[level]

	for n in range(1, 10):
		if n not in row[x] and n not in col[y] and n not in square[x//3][y//3]:
			board[x][y] = n
			row[x].add(n)
			col[y].add(n)
			square[x//3][y//3].add(n)

			search(level+1)

			board[x][y] = 0
			row[x].remove(n)
			col[y].remove(n)
			square[x//3][y//3].remove(n)

pos = []
for i in range(9):
	for j in range(9):
		cur = board[i][j]
		if cur == 0:
			pos.append((i,j))
		else:
			row[i].add(board[i][j])
			col[j].add(board[i][j])
			square[i//3][j//3].add(board[i][j])

search(0)