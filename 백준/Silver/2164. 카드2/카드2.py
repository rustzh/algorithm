import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(1, N+1):
	q.append(i)

result = q.popleft()
while q:
	v = q.popleft()
	q.append(v)

	result = q.popleft()

print(result)