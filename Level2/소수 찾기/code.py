import itertools

def solution(numbers):
    answer = 0
    list_num = [num for num in numbers]
    nPr = []
    list_npr = []
    
    for i in range(1,len(list_num)+1):
        nPr = nPr + list(itertools.permutations(list_num,i))
    
    for num in set(nPr):
        #print(num)
        num=int(''.join(num))
        if prime_list(num) == True:
            list_npr.append(num)
    #print(list_npr)        
    answer = len(set(list_npr))
    
    return answer

def prime_list(num):
    if num ==0 or num ==1:
        return False
    else:
        m = int(num ** 0.5)
        for i in range(2, m+1):
            if num % i == 0:
                return False
        return True
    

if __name__ == '__main__':
    print(solution(numbers))