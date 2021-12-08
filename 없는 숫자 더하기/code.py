def solution(numbers):
    answer = 0
    for num in range(10):
        if num not in numbers:
            answer = answer + num
    return answer


if __name__ == '__main__':
    print(solution(numbers))