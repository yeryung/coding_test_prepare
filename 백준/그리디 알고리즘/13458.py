from sys import stdin
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
b,c = map(int,stdin.readline().split())

# 필요한 감독관의 최소 수
cnt = 0

for i in a:
    if i <= b:
        cnt += 1
    else:
        cnt += 1
        tmp = i - b
        if tmp % c == 0:
            cnt += tmp//c
        else:
            cnt += tmp//c + 1
print(cnt)