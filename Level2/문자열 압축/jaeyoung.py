def solution(s):
    answer = 98999999999
    
    
    has = {}
    if(len(s)==1):
        answer = 1
    for i in range(1, len(s)//2 + 1):
        has = []
        recent = ""
        result = 0
        b = 0
        temp = ""
        for a in range(0, len(s), i):
            temp = s[a:a+i]
            if(recent == ""):
                if(b == 0):
                    b = 1
                else:
                    b += 1
            elif(recent == temp):
                b+=1
            else:
                has.append(str(b) + "," + recent)
                b = 1
            recent = temp
        has.append(str(b) + "," + recent)
        
        for a in has:
            l = a.split(",")
            b = int(l[0])
            if(b != 1):
                result += len(a) - 1
            else:
                result += len(a) - 2
                
        if(result < answer):
            answer = result
        
        
    return answer