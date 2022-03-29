from sys import stdin

n = stdin.readline().strip()
a = []
sum = 0

# 0을 포함하지 않으면 30의배수가 될 수 없음
for i in n:
    a.append(i)
    sum += int(i)

if '0' not in a:
    print(-1)
else:
    if sum % 3 != 0:
        print(-1)
    else:
        a.sort(reverse=True)
        output = ''.join(s for s in a)
        print(output)