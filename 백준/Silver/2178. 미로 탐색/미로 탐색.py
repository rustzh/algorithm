from collections import deque

moves = [(0,1), (-1,0), (0,-1), (1,0)]

N, M = map(int, input().split())
miro = [[] for _ in range(N)]
for i in range(N):
	miro[i] = input()

min_values = [[0]*M for _ in range(N)]
min_values[0][0] = 1
visited = [[False]*M for _ in range(N)]

q = deque()
q.append((0,0))
visited[0][0] = True

while q:
	(n, m) = q.popleft()

	for move in moves:
		cur_n = n+move[0]
		cur_m = m+move[1]
		if 0<=cur_n<N and 0<=cur_m<M and miro[cur_n][cur_m]=='1' and visited[cur_n][cur_m]==False:
			if min_values[cur_n][cur_m]>1:
				min_values[cur_n][cur_m] = min(min_values[cur_n][cur_m], min_values[n][m]+1)
			else:
				min_values[cur_n][cur_m] = min_values[n][m]+1
			q.append((cur_n, cur_m))
			visited[cur_n][cur_m] = True

print(min_values[N-1][M-1])