from itertools import combinations

n, s = map(int, input().split())
lst = list(map(int, input().split()))

cnt=0

for i in range(1, n+1):
	for comb in combinations(lst, i):
		nsum = 0
		for u in comb:
			nsum+=u
		if nsum==s:
			cnt+=1

print(cnt)