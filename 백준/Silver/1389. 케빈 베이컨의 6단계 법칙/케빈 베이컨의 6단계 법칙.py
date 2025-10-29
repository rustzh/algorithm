from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
ans = 0

for i in range (m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range (n+1):
    graph[a].sort()
    
minkb = 0
for i in range(1, n+1):
    kb = 0
    for j in range(1, n+1):
        if i==j: continue
        q = deque()
        visited = [False]*(n+1)
        phase = 0
        visited[i] = True
        q.append(i)
        q.append(phase)
        data=i
        while q:
            data = q.popleft()
            result = q.popleft()
            if data == j: 
                break
            phase = result+1
            for w in graph[data]:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
                    result = q.append(phase)
        kb += result
    if (minkb==0 or minkb>kb): 
        minkb = kb
        ans = i
    
print(ans)