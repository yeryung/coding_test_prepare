from sys import stdin

def count(mid):
    cnt = 1
    ep = x[0]

    for i in range(len(x)):
        if x[i]-ep >= mid:
            cnt += 1
            ep = x[i]
    return cnt

n,c = map(int,stdin.readline().split())
x = []

for _ in range(n):
    x.append(int(stdin.readline()))

x.sort()

# 이분 탐색
start = 1
end = x[n-1]
res = 0

while start <= end:
    mid = (start + end) //2

    if count(mid) >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
