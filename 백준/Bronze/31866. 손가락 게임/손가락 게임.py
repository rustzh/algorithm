a, b = map(int, input().split())

items = [0, 2, 5]

def game(a, b):
	if a == 0:
		if b == 0:
			return '='
		if b == 5:
			return '<'
		else:
			return '>'
	if a == 2:
		if b == 2:
			return '='
		if b == 0:
			return '<'
		else:
			return '>'
	if a == 5:
		if b == 5:
			return '='
		if b == 2:
			return '<'
		else:
			return '>'
	else:
		if b in items:
			return '<'
		else:
			return '='
		
print(game(a, b))