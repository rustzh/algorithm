import sys

having = {}
N = int(sys.stdin.readline().rstrip())
my_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

for card in my_cards:
	if card in having:
		having[card] += 1
	else:
		having[card] = 1

for i in range(M):
	if cards[i] in having:
		print(having[cards[i]], end=' ')
	else:
		print(0, end=' ')
