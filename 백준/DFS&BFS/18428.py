# N*N 크기 복도 
# 3개의 장애물을 설치 
# 장애물 설치 => 모든 경우의 수 
# dfs/bfs로 탐색 or combination 이용
from sys import stdin
from itertools import combinations

# 학생 발견 : false 장애물 발견 : True
def check(teacher_x,teacher_y,direction):
    # 이동 상하좌우 다 확인하기
    if direction == 0:
        while teacher_y >= 0:
            if data[teacher_x][teacher_y] == 'S':
                return False
            if data[teacher_x][teacher_y] == 'O':
                return True
            teacher_y -= 1

    if direction == 1:
        while teacher_y < n :
            if data[teacher_x][teacher_y] == 'S':
                return False
            if data[teacher_x][teacher_y] == 'O':
                return True
            teacher_y += 1
    
    if direction == 2:
        while teacher_x >= 0 :
            if data[teacher_x][teacher_y] == 'S':
                return False
            if data[teacher_x][teacher_y] == 'O':
                return True
            teacher_x -= 1
    
    if direction == 3:
        while teacher_x < n:
            if data[teacher_x][teacher_y] == 'S':
                return False
            if data[teacher_x][teacher_y] == 'O':
                return True
            teacher_x += 1

       
def process():
    for x,y  in teacher_list:
        for i in range(4):
            # 학생이 발견될 경우 return False
            if check(x,y,i) == False:
                return False
    return True
    

if __name__ == '__main__':
    n = int(stdin.readline())
    data = []
    teacher_list = []
    spaces = []

    stu_pass = False

    for _ in range(n):
        data.append(list(map(str, stdin.readline().split())))

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                teacher_list.append((i,j))
            if data[i][j] == 'X':
                spaces.append((i,j))
    
    # 빈공간에서 3개를 뽑는 경우의 수
    for combi in combinations(spaces,3):
        for x,y in combi:
            data[x][y] = 'O'
        
        # 학생이 감지되지 않은 경우
        if process() == True:
            stu_pass = True
            break

        for x,y in combi:
            data[x][y] = 'X'

    if stu_pass == True:
        print('YES')
    else:
        print('NO')