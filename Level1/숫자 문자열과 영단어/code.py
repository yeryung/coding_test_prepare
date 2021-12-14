import re

def solution(s):
    answer = 0
    s = re.sub(r'one+','1',s)
    s = re.sub(r'two+','2',s)
    s = re.sub(r'three+','3',s)
    s = re.sub(r'four+','4',s)
    s = re.sub(r'five+','5',s)
    s = re.sub(r'six+','6',s)
    s = re.sub(r'seven+','7',s)
    s = re.sub(r'eight+','8',s)
    s = re.sub(r'nine+','9',s)
    s = re.sub(r'zero+','0',s)
    
    answer = int(s)
    
    return answer


if __name__ == '__main__':
    print(solution(s))

"""
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

"""    