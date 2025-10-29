from itertools import permutations

def fact(x):
	if x==0:
		return 1
	return fact(x-1)*x

lst = input()

cnt=0
for cur in permutations(lst):
	possible = True
	for i in range(0, len(lst)-1):
		if cur[i]==cur[i+1]:
			possible = False
			break
	if possible==True:
		cnt+=1

for i in range(ord('a'), ord('z')+1):
	cnt //= fact(lst.count(chr(i)))
	
print(cnt)