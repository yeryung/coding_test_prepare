from sys import stdin

def DFS(x,cnt):
    global tmp,output
    if x == 1:
        if output > cnt:
            output = cnt
    else:
        for _x,_y in a_list:
            if tmp == _y:
                tmp = _x
                DFS(tmp,cnt+1)
                tmp = n
            
a_list = []
n,m = map(int,stdin.readline().split())

for i in range(m):
    a,b = map(int,stdin.readline().split())
    a_list.append((a,b))

a_list.sort(key=lambda x : (x[1],x[0]),reverse=True)

tmp = n
output = 2147000000
DFS(n,0)

if output == 2147000000:
    print(-1)
else:
    print(output)