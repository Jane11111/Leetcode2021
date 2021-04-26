# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 10:00
# @Author  : zxl
# @FileName: M001.py


import sys
import numpy as np
# def solve(s,ops):
#     arr = [0 for i in range(len(s)+1)]
#     num = 26
#     for i,j,k in ops:
#         for m in range(i,j+1):
#             arr[m] = (arr[m]+26-k)%26 # 数字往右移动的位数
#
#     new_s = ''
#     for i in range(len(s)):
#
#         ops_value = arr[i+1]
#         iv = ord(s[i])-ord('a')
#         iv2 = (iv+ops_value)%26
#         new_c = chr(iv2+ord('a'))
#         new_s+=new_c
#     return new_s

def solve2(s,arr):
    new_s = ''
    for i in range(len(s)):
        ops_value = arr[i + 1]
        iv = ord(s[i]) - ord('a')
        iv2 = (iv + ops_value) % 26
        new_c = chr(iv2 + ord('a'))
        new_s += new_c
    return new_s

if __name__ == "__main__":
    # 读取第一行的n
    s = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())

    ops = []
    arr = np.array([0 for i in range(len(s) + 1)])
    for i in range(n):
        line = sys.stdin.readline().strip()
        x,y,k = list(map(int, line.split()))
        # for m in range(x,y+1):
        #     arr[m] +=26-k# 数字往右移动的位数
        arr[x:y+1]+=(26-k)


    ans = solve2(s,arr)
    print(ans)
