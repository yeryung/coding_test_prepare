def solution(progresses, speeds):
    answer = []
    stack = []
    progress_speed = list(zip(progresses,speeds))
    count = 0
    
    for i, j in enumerate(progress_speed):
        progress = 100 - j[0]
        
        if progress % j[1] == 0:
            day = progress // j[1]
        else:
            day = progress // j[1] + 1
            
        if i == 0:
            stack.append(day)
        else:
            if stack[0] >= day:
                stack.append(day)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(day)
    
    answer.append(len(stack))

    return answer

if __name__== "__main__":
    print(solution(progresses,speeds))