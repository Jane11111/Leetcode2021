# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 10:49
# @Author  : zxl
# @FileName: M004.py

import sys

def solve(matrix):
    n = len(matrix)
    count = 0

    for sx in range(n):
        for sy in range(n):


            for ex in range(sx,n):
                for ey in range(sy,n):
                    if matrix[ex][ey] == '#':
                        break
                    f = True
                    for i in range(sx,ex+1):
                        for j in range(sy,ey+1):
                            if matrix[i][j] == '#':
                                f = False
                                break
                        if not f:
                            break
                    if f:
                        count+=1
    return count


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