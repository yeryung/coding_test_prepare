from sys import stdin

rope = []
output = -2147000000
n = int(stdin.readline())

for _ in range(n):
    a = int(stdin.readline())
    rope.append(a)

rope.sort(reverse=True)

while rope:
    w = rope[-1]*len(rope)
    if w > output:
        output = w
    rope.pop()

print(output)
