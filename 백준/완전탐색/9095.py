from sys import stdin

def DFS(L,sum):
    global cnt
    if sum > n:
        return
    if sum == n:
        cnt += 1
    else:
        for i in range(1,4):
            DFS(L+1,sum+i)

n_list = []
t = int(stdin.readline())

for i in range(t):
    cnt = 0
    n = int(stdin.readline())
    DFS(0,0)
    print(cnt)
    