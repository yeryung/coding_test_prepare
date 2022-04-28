from sys import stdin

x,y = map(int,stdin.readline().split())

# 게임 최소 추가 횟수
start = 0
end = 1000000000
z = int(y/x*100)
output = 1000000000

if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end)//2
        dy = y + mid
        dx = x + mid
        new_z = int(dy/dx*100)
        if new_z > z:
            end = mid - 1
        else:
            start = mid + 1

print(end+1)