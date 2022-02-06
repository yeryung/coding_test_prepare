# 도시의 개수 : N , 도로의 개수 : M , 거리 정보 : K, 출발 도시의 정보 : X
# bfs니까 Queue이용하기 
from collections import deque
from sys import stdin

def bfs(city_info,X, distance_list):
    distance_list[X] = 0

    queue = deque([X])
    
    # bfs 구현
    while queue:
        tmp = queue.popleft()

        for i in city_info[tmp]:
            if distance_list[i] == -1:
                distance_list[i] = distance_list[tmp] + 1
                queue.append(i)

    # 최단거리가 K인 도시 출력하기
    for i in range(len(distance_list)):
        if distance_list[i] == K:
            print(i)
    
    if K not in distance_list:
        print(-1)
    
    

if __name__ == '__main__':
    dis = 0
    N, M, K, X = map(int, stdin.readline().split())

    city_info = [[] for i in range(N+1)]
    distance_list = [-1] * (N+1)

    # M개의 줄만큼 정보 받기
    # 두 개의 자연수 A, B

    for i in range(M):
        A, B = map(int, stdin.readline().split())
        city_info[A].append(B)

    bfs(city_info, X , distance_list)

# [[1,2],[1,3],[2,3],[2,4]]
# 최단거리가 K인 모든 도시의 번호를 출력


