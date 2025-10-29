T = int(input())

for test_case in range(T):
	results = input()
	
	score = 0
	cnt = 0
	for result in results:
		if result == 'O':
			cnt += 1
			score += cnt
		if result == 'X':
			cnt = 0
			
	print(score)