n = int(input())

players = [tuple(map(int, input().split())) for _ in range(n)]
scores = []

for player in players:
	score = []

	score.append(player[1]*player[2]*player[3])
	score.append(player[1]+player[2]+player[3])
	score.append(player[0])

	scores.append(score)

winner = sorted(scores)

for i in range(3):
	print(winner[i][2], end=' ')