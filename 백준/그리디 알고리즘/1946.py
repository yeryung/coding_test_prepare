from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    grade = []
    for _ in range(n):
        a,b = map(int,stdin.readline().split())
        grade.append((a,b))
    grade.sort()

    highest = n+1
    cnt = 0

    for j,k in grade:
        if k < highest:
            cnt += 1
            highest = k
    
    print(cnt)