N = int(input())
K = input()

odd = 0
even = 0

for i in range(N):
	if K[i]==0 or int(K[i])%2==0:
		even+=1
	else:
		odd+=1

if odd > even:
	print(1)
elif odd < even:
	print(0)
else:
	print(-1)