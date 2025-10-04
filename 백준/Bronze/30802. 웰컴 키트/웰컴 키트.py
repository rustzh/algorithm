N = int(input())
Tsize = list(map(int, input().split()))
T, P = map(int, input().split())

Tcnt = 0
for size in Tsize:
	if size == 0:
		continue
	Tcnt += size//T
	if size%T > 0:
		Tcnt += 1

print(Tcnt)
print(N//P, N%P)