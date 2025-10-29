N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst1 = sorted(lst)

for u in lst1:
	print(' '.join(map(str, u)))