from sys import stdin

n = int(stdin.readline())
time = sorted(list(map(int,stdin.readline().split())))
a = [0 for _ in range(n+1)]

for i in range(1,n+1):
    a[i] = a[i-1] + time[i-1]

print(sum(a))