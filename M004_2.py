# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 11:43
# @Author  : zxl
# @FileName: M004_2.py

import sys

def solve(matrix):
    pass



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    matrix = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        lst = []
        for c in line:
            lst.append(c)
        matrix.append(lst)
    ans = solve(matrix)
    print(ans)