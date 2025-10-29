import sys

n = int(sys.stdin.readline())
infos = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0

for info in infos:
	if left<=right:
		left+=info
	else:
		right+=info

w = abs(left-right)
cnt = 0
weights = [100,50,20,10,5,2,1]

for weight in weights:
	cnt += w//weight
	w %= weight

print(cnt)