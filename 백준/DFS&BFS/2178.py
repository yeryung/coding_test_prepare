from sys import stdin
from collections import deque

board = []
N,M = map(int,stdin.readline().split())

for _ in range(N):
    tmp_list = []
    tmp = stdin.readline().strip()
    for i in tmp:
        tmp_list.append(int(i))
    board.append(tmp_list)

dis = [[0]*M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0))
board[0][0] = 0
dis[0][0] = 1

while q:
    x,y = q.popleft()
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0<=_x<=N-1 and 0<=_y<=M-1 and board[_x][_y] == 1:
            board[_x][_y] = 0
            dis[_x][_y] = dis[x][y] + 1
            q.append((_x,_y))

print(dis[N-1][M-1])
