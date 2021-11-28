def solution(array, commands):
    answer = []
    
    for i in commands:
        newdata = array[i[0]-1:i[1]]
        newdata.sort()
        answer.append(newdata[i[2]-1])
    return answer