from sys import stdin
from bisect import bisect_left,bisect_right

def count_range(left_value,right_value):
    right_index = bisect_right(n_list,right_value)
    left_index = bisect_left(n_list,left_value)

    return right_index-left_index



n = int(stdin.readline())
n_list = sorted(list(map(int,stdin.readline().split())))

m = int(stdin.readline())
m_list = list(map(int,stdin.readline().split()))


for target in m_list:
    print(count_range(target,target),end = " ")