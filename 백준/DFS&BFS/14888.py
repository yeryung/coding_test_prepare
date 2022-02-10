# 모든 가능한 경우의 수 구해야 할 것 같습니다.
# 연산자 우선순위는 무시함.
from sys import stdin

def dfs(i, now):
    global min_value,max_value,add,sub,mul,div
    
    if i == N:
        min_value = min(min_value,now)
        max_value = max(max_value,now)
   
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-num_list[i])
            sub +=1
        if mul > 0:
            mul -= 1
            dfs(i+1,now*num_list[i])
            mul +=1
        if div > 0:
            div -= 1
            dfs(i+1,-(-now // num_list[i]) if now < 0 else now // num_list[i])
            div +=1
    
        
if __name__ == '__main__': 
    min_value = 1e9
    max_value = -1e9       

    N = int(stdin.readline())

    # N개 숫자 받기
    num_list = list(map(int,stdin.readline().split()))

    # 연산자 개수 받기
    add,sub,mul,div = map(int,stdin.readline().split())

    dfs(1,num_list[0])

    print(max_value)
    print(min_value)