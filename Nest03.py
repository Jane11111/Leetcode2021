# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 15:23
# @Author  : zxl
# @FileName: Nest03.py

import sys
import math
# import numpy as np
def solve(N,K,lst):

    ans = []
    for arr in lst:
        # k = np.argmax(arr)
        # v = np.exp(arr[k])/np.sum(np.exp(arr))
        k = 0
        exp_lst = [0. for i in range(K)]
        for i in range(len(arr)):
            exp_lst[i] = math.exp(arr[i])
            if arr[i]>arr[k]:
                k = i
        v = exp_lst[k]/sum(exp_lst)
        ans.append([k,v])
    return ans

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    N,K = list(map(int, line.split()))

    lst = []
    while N:
        line = sys.stdin.readline().strip()
        arr = list(map(float, line.split()))
        lst.append(arr)
        N-=1
    ans = solve(N,K,lst)
    for arr in ans:
        # print(arr[0],' ','%.6f'%(arr[1]))
        print('%d %.6f'%(arr[0],arr[1]))

