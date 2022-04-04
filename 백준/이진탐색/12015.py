from sys import stdin

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))

check = [a[0]]
lt = a[0]
rt = a[n-1]

while lt<rt:
    for i in range(1,n):
        if lt < a[i]:
            lt = a[i]
            check.append(lt)

print(len(check))