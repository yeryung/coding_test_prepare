from itertools import combinations

def solution(nums):
    answer = -1
    sum = 0
    combination = list(combinations(nums,3))
    is_prime = []
    
    for tuple_num in combination:
        sum = 0
        for num in tuple_num:
            sum += num
        if check_prime(sum) == True:
            is_prime.append(sum)
    answer = len(is_prime)
    return answer

def check_prime(sum):
    if sum == 0 or sum == 1:
        return False
    else:
        m = int(sum ** 0.5)
        for i in range(2, m+1):
            if sum % i == 0:
                return False
        return True


if __name__ == '__main__':
    print(solution(nums))