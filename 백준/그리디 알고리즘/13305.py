from sys import stdin

n = int(stdin.readline())
length = list(map(int,stdin.readline().split()))
price = list(map(int,stdin.readline().split()))

cost = 0
minest = price[0]

for i in range(n-1):
    if price[i] < minest:
        minest = price[i]
    cost += minest * length[i]

print(cost)