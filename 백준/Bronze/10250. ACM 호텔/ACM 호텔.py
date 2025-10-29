T = int(input())

for test_case in range(T):
	H, W, N = map(int,input().split())

	if N%H == 0:
		h = H
		w = N//H
	else:
		h = N%H
		w = N//H + 1

	if w < 10:
		print(f'{h}0{w}')
	else:
		print(f'{h}{w}')