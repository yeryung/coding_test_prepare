def solution(numbers):
    answer = ''
    list_num = []
    for number in numbers:
        number = str(number)
        list_num.append(number)
         
    list_num.sort(key = lambda x: x*3, reverse=True)

    for key in list_num:
        answer = answer + key

    return str(int(answer))

if __name__ == "__main__":
    print(solution(numbers))