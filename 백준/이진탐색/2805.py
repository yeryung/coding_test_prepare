from sys import stdin

def count(mid):
    sum = 0
    for tree in trees:
        if tree <= mid:
            continue
        else:
            tmp = tree - mid
            sum += tmp
    return sum

n,m = map(int,stdin.readline().split())
trees = list(map(int,stdin.readline().split()))

largest = max(trees)
res = 0

#이분 탐색
start = 1
end = largest

while start <= end:
    mid = (start + end)//2
    if count(mid) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)