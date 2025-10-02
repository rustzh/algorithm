from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
	arr[i] = list(input())
	for j in range(M):
		if arr[i][j] == "I":
			start_r = i
			start_c = j
			visited[start_r][start_c] = 1
		if arr[i][j] == "X":
			visited[i][j] = 1

r_dir = [1, 0, -1, 0]
c_dir = [0, 1, 0, -1]

cnt = 0
q = deque()
q.append((start_r, start_c))

while q:
	r, c = q.popleft()

	for i in range(4):
		cur_r = r + r_dir[i]
		cur_c = c + c_dir[i]

		if cur_r < 0 or cur_r >= N or cur_c < 0 or cur_c >= M:
			continue
		if visited[cur_r][cur_c] == 1:
			continue

		visited[cur_r][cur_c] = 1
		q.append((cur_r, cur_c))
		if arr[cur_r][cur_c] == 'P':
			cnt += 1

print(cnt) if cnt != 0 else print("TT")