n = int(input())
cont = list(map(int,input().split()))
total = sum(cont)
h = total // n
x = total % n

cnt = 0
for i in range(n):
	if cont[i]>h:
		if x>0:
			cnt+=cont[i]-h-1
			x-=1
		else:
			cnt+=cont[i]-h

print(cnt)