# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 20:19
# @Author  : zxl
# @FileName: Tencent.py


import sys

def solve(mat,n,m):
    newmat = [[] for i in range(m)]

    for j in range(m):
        for i in range(n):
            newmat[j].append(mat[i][j])

    prob = 1/n
    ans = 0
    for i in range(m):
        tmp = [item for item in newmat[i]]
        tmp.sort()
        sum_val = 0
        for j in range(n):
            sum_val += tmp[j]
            # sum_val *= prob
            ans+=sum_val*prob
    return ans


if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n,m = list(map(int, line.split()))

    mat = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        arr = list(map(int, line.split()))
        mat.append(arr)
    ans = solve(mat,n,m)
    print('%.6f'%ans)
