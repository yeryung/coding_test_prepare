from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

# data / virus data
data = []
virus_list = []

for i in range(N):
    data.append(list(map(int,stdin.readline().split())))
    # 해당위치에 바이러스가 존재하는 경우
    # 바이러스의 종류, 바이러스 시간,바이러스의 위치 저장하기
    for j in range(N):
        if data[i][j] != 0:
            virus_list.append((data[i][j],0,i,j))
virus_list.sort()

q = deque(virus_list)

target_s, target_x, target_y = map(int, stdin.readline().split())

dx =[-1,0,1,0]
dy = [0,1,0,-1]

# bfs 실행
while q:
    virus,s, x, y = q.popleft()

    if s == target_s:
        break

    # 네가지 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<N and ny >=0 and ny <N:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
                
print(data[target_x-1][target_y-1])
