from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

graph=[[] for _ in range(N+1)]
degree = [0]*(N+1)

for i in range(M):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()


for j in range(1,N+1):
    if degree[j] == 0:
        q.append(j)

while q:
    tmp = q.popleft()
    print(tmp,end=' ')
    for k in graph[tmp]:
        degree[k]-=1
        if degree[k] == 0:
            q.append(k)