def solution(priorities, location):
    answer = 0
    p = priorities
    count = 1
    while(len(p)!=0):
        a = p[0]
        s = sorted(p)
        if(s[len(p) - 1] > a):
            if(location == 0):
                location = len(p) - 1
            else:
                location = location - 1
            p.append(p.pop(0))
        else:
            if(location == 0):
                answer = count
                break
            else:
                p.pop(0)
                print(p)
                location = location - 1
                count+=1
                
        print(p)
    return answer