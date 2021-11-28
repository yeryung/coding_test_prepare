def solution(phone_book):
    answer = True
    
    sortbook = sorted(phone_book)
    
    #바로앞에 옴
    for i in range(0,len(sortbook) - 1):
        #앞자리에서 찾으면
        if (sortbook[i+1].find(sortbook[i]) == 0):
            answer = False
            break

    return answer