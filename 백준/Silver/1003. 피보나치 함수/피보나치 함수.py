zero_and_one = [[0, 0] for _ in range(41)]
zero_and_one[0] = [1, 0]
zero_and_one[1] = [0, 1]

for i in range(2, 41):
	zero_and_one[i] = [zero_and_one[i-1][0]+zero_and_one[i-2][0], zero_and_one[i-1][1]+zero_and_one[i-2][1]]

T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	result = " ".join(map(str, zero_and_one[N]))
	print(result)