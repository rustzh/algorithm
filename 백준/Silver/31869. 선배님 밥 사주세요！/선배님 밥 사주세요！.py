date = [[-1] for i in range(70)]
memo = {}
money = {}

N = int(input())

for i in range(N):
	S, W, D, P = input().split()
	D = (int(W)-1)*7 + int(D)

	if date[D][0] == -1:
		date[D].pop(0)
	date[D].append(S)
	memo[S] = int(P)

for i in range(N):
	S, P = input().split()
	money[S] = int(P)

result = 0
cnt = 0
for i in range(70):
	B = 0
	for s in date[i]:
		if s == -1:
			continue
		if memo[s] <= money[s] and B == 0:
			cnt+=1
			result = max(result, cnt)
			B = 1
	if B==1:
		continue
	else:
		cnt = 0


print(result)