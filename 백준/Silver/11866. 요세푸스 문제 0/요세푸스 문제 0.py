from collections import deque

N, K = map(int, input().split())
q = deque(i for i in range(1,N+1))

print("<", end="")
cnt = K
while q:
	a = q.popleft()
	cnt -= 1
	if cnt == 0:
		if not q:
			print(a, end=">")
		else:
			print(a, end=", ")

		cnt = K
	else:
		q.append(a)