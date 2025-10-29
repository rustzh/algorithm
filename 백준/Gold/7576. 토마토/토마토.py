from collections import deque

M, N = map(int,input().split())
# NxM 상자

q1 = deque()
q2 = deque()
moves = [(-1,0), (1,0), (0,-1), (0,1)]

tomatos = [[] for _ in range(N)]
for i in range(N):
	tomatos[i] = list(map(int, input().split()))
	for j in range(M):
		if tomatos[i][j] == 1:
			q1.append((i, j, 0))

result = 0
while q1:
	(y, x, d) = q1.popleft()
	result = d

	for move in moves:
		dy = y+move[0]
		dx = x+move[1]

		if 0<=dy<N and 0<=dx<M and tomatos[dy][dx]==0:
			tomatos[dy][dx] = 1
			q1.append((dy,dx,d+1))

for row in tomatos:
    if 0 in row:
        result = -1

print(result)