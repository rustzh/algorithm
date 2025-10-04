N, M = map(int, input().split())
arr = list(map(int, input().split()))

neg = []
pos = []

for x in arr:
	if x > 0:
		pos.append(x)
	else:
		neg.append(-x)

neg = sorted(neg)[::-1]
pos = sorted(pos)[::-1]

dists = []
for x in neg[::M]:
	dists.append(x)
for x in pos[::M]:
	dists.append(x)

print(2*sum(dists) - max(dists))