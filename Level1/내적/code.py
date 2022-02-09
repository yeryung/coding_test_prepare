import numpy as np

def solution(a, b):
    answer = 1234567890
    v1 = np.array(a)
    v2 = np.array(b)
    answer = np.dot(v1,v2)
    return answer

if __name__ == '__main__':
    print(solution(a,b))