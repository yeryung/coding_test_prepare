def solution(record):
    answer = []
    
    idlist = {}
    
    for i in record:
        l = i.split(" ")
        if l[0] == "Enter" :
            idlist[l[1]] = l[2]
        elif l[0] == "Change":
            idlist[l[1]] = l[2]
    
    for i in record:
        l = i.split(" ")
        if l[0] == "Enter":
            answer.append(idlist[l[1]] + "님이 들어왔습니다.")
        elif l[0] == "Leave":
            answer.append(idlist[l[1]] + "님이 나갔습니다.")
            

            
            
        
                
            
    
    return answer