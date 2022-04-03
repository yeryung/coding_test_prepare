from sys import stdin

def budget(mid):
    sum = 0
    for i in money:
        if i <= mid:
            sum += i
        else:
            sum += mid
    return sum

n = int(stdin.readline())
money = list(map(int,stdin.readline().split()))
m = int(stdin.readline())

lt = 0
rt = max(money)
output = -2147000000

while lt<=rt:
    mid = (lt+rt)//2
    if budget(mid) <= m:
        output = max(output,mid)
        lt = mid + 1
    else:
        rt = mid - 1

print(output)