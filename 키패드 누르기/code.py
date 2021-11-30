def solution(numbers, hand):
    answer = ''
    # '*'
    lposition = 10
    # '#'
    rposition = 11
    
    left = [1,4,7]
    right = [3,6,9]
    
    distance_two = [3,1,0,1,2,1,2,3,2,3,4,4]
    distance_five = [2,2,1,2,1,0,1,2,1,2,3,3]
    distance_eight = [1,3,2,3,2,1,2,1,0,1,2,2]
    distance_zero = [0,4,3,4,3,2,3,2,1,2,1,1]
    
    for number in numbers:
        if number in left:
            answer = answer + 'L'
            lposition = number
        elif number in right:
            answer = answer + 'R'
            rposition = number
        else:
            if number == 2:
                if distance_two[lposition] > distance_two[rposition]:
                    answer = answer + 'R'
                    rposition = number
                elif distance_two[lposition] < distance_two[rposition]:
                    answer = answer + 'L'
                    lposition = number
                else:
                    if hand == 'left':
                        answer = answer + 'L'
                        lposition = number
                    else:
                        answer = answer + 'R'
                        rposition = number
                        
            elif number == 5:
                if distance_five[lposition] > distance_five[rposition]:
                    answer = answer + 'R'
                    rposition = number
                elif distance_five[lposition] < distance_five[rposition]:
                    answer = answer + 'L'
                    lposition = number
                else:
                    if hand == 'left':
                        answer = answer + 'L'
                        lposition = number
                    else:
                        answer = answer + 'R'
                        rposition = number
            elif number == 8:
                if distance_eight[lposition] > distance_eight[rposition]:
                    answer = answer + 'R'
                    rposition = number
                elif distance_eight[lposition] < distance_eight[rposition]:
                    answer = answer + 'L'
                    lposition = number
                else:
                    if hand == 'left':
                        answer = answer + 'L'
                        lposition = number
                    else:
                        answer = answer + 'R'
                        rposition = number
            else:
                if distance_zero[lposition] > distance_zero[rposition]:
                    answer = answer + 'R'
                    rposition = number
                elif distance_zero[lposition] < distance_zero[rposition]:
                    answer = answer + 'L'
                    lposition = number
                else:
                    if hand == 'left':
                        answer = answer + 'L'
                        lposition = number
                    else:
                        answer = answer + 'R'
                        rposition = number
            
    return answer


if __name__ == "__main__":
    print(solution(numbers,hand))