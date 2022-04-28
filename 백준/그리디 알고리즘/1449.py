from sys import stdin

n,l = map(int,stdin.readline().split())
position = list(map(int,stdin.readline().split()))
position.sort()

lt = position[0]
rt = position[0]+l
cnt = 1

for i in position:
    if lt <= i < rt:
        continue
    else:
        lt = i
        rt = i + l
        cnt += 1

print(cnt)