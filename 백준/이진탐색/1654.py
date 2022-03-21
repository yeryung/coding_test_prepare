from sys import stdin

def count(mid):
    cnt = 0
    for line in lines:
        cnt += line//mid
    return cnt

k,n = map(int,stdin.readline().split())
lines = []
largest = 0

for _ in range(k):
    tmp = int(stdin.readline())
    lines.append(tmp)
    largest = max(largest,tmp)

# 이분탐색
start = 1
end = largest

while start<=end:
    mid = (start+end)//2
    if count(mid) >= n:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)