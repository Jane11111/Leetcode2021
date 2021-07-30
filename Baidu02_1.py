# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 15:36
# @Author  : zxl
# @FileName: Baidu02_1.py


def solve(mat):

    n = len(mat)


    s = 0
    e = n-1

    while s<e:

        for i in range(s,e):

            mat[s][i],mat[i][e],mat[e][e-(i-s)],mat[e-(i-s)][s] = \
                mat[e-(i-s)][s] ,mat[s][i],mat[i][e],mat[e][e-(i-s)]

        s+=1
        e-=1


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
solve(mat)
print(mat)
