from sys import stdin
from collections import deque

n,k = map(int,stdin.readline().split())
MAX = 100000
ch = [0] * (MAX+1)
res = [0] * (MAX+1)
ch[n] = 1

q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        break
    else:
        for next in (x-1,x+1,2*x):
            if 0<=next<=MAX and ch[next] == 0:
                q.append(next)
                ch[next] = 1
                res[next] = res[x] + 1

print(res[k])