from sys import stdin

n,m,k = map(int,stdin.readline().split())

q1 = n//2
q2 = m//1
output = min(q1,q2)

r1 = n-output*2
r2 = m-output*1
tol = r1+r2

while True:
    if tol >= k:
        break
    else:
        output -= 1
        tol += 3

print(output)