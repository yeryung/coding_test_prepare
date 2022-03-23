from sys import stdin

n = int(stdin.readline())

meeting = []
for _ in range(n):
    s,e = map(int,stdin.readline().split())
    meeting.append((s,e))

# 끝나는 시간으로 sort
meeting.sort(key = lambda x: (x[1],x[0]))

ep = 0
cnt = 0

for s,e in meeting:
    if s >= ep:
        cnt += 1
        ep = e

print(cnt)