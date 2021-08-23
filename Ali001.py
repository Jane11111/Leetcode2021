# -*- coding: utf-8 -*-
# @Time    : 2021-08-09 19:02
# @Author  : zxl
# @FileName: Ali001.py


import sys

def solve(arr):
    L = sum(arr)

    dic = {}

    sum_val = 0
    sum_dic = {}
    for i in range(len(arr)):

        num = arr[i]
        sum_val += num
        sum_dic[i] = sum_val

        if sum_val not in dic:
            dic[sum_val] = True

        for j in range(i):

            tmp = sum_val - sum_dic[j]
            if tmp not in dic:
                dic[tmp] = True
    return 0 not in dic and len(dic) == L



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    while T:

        N = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        arr = list(map(int, line.split()))
        ans = solve(arr)
        if ans:
            print('YES')
        else:
            print('NO')


        T-=1

