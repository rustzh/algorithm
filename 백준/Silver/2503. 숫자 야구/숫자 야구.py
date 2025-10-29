from itertools import permutations

N = int(input())
qna = [tuple(map(int, input().split())) for _ in range(N)]

cnt=0
for cur in permutations(range(1, 10), 3):
	possible = True

	for u in qna:
		num = str(u[0])

		strike = 0
		ball = 0

		for i in range(3):
			if int(num[i])==cur[i]:
				strike+=1
			else:
				if str(cur[i]) in num:
					ball+=1

		if strike!=u[1] or ball!=u[2]:
			possible = False

	if possible == True:
		cnt+=1 

print(cnt)