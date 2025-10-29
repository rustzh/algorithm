from collections import deque

def dfs(node):
	visited[node] = True
	print(node, end=' ')

	for adj_node in adj_list[node]:
		if visited[adj_node] == True:
			continue
		dfs(adj_node)


N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

for lst in adj_list:
	lst.sort()

dfs(V)

print()
visited = [False] * (N+1)

q = deque()
q.append(V)
visited[V] = True

while q:
	node = q.popleft()
	print(node, end=' ')

	for adj_node in adj_list[node]:
		if visited[adj_node] == True:
			continue
		q.append(adj_node)
		visited[adj_node] = True