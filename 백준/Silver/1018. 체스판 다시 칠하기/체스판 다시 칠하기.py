N, M = map(int, input().split())
board = [input() for _ in range(N)]
W = ['WBWBWBWB'] + ['BWBWBWBW'] + ['WBWBWBWB'] +['BWBWBWBW'] +['WBWBWBWB'] + ['BWBWBWBW'] +['WBWBWBWB'] +['BWBWBWBW']
B = ['BWBWBWBW'] +['WBWBWBWB'] +['BWBWBWBW'] +['WBWBWBWB'] +['BWBWBWBW'] +['WBWBWBWB'] +['BWBWBWBW'] +['WBWBWBWB']

ans = 10000
for n in range(N-7):
	for m in range(M-7):
		now_w = 0
		now_b = 0
		for i in range(8):
			for j in range(8):
				if board[n+i][m+j] != W[i][j]:
					now_w += 1
				if board[n+i][m+j] != B[i][j]:
					now_b += 1
		ans = min(ans, now_b, now_w)

print(ans)