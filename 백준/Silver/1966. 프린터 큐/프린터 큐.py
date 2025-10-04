from collections import deque

T = int(input())

for _ in range(T):
	N, M = map(int, input().split())

	q = deque()
	pr = list(map(int, input().split()))
	max_pr_list = sorted(pr)
	max_pr_idx = N-1

	for i in range(N):
		q.append((i, pr[i]))

	cnt = 0
	while q:
		doc = q.popleft()

		if doc[1] == max_pr_list[max_pr_idx]:
			cnt += 1
			if doc[0] == M:
				print(cnt)
				break
			max_pr_idx -= 1
		else:
			q.append(doc)