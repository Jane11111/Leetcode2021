# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 15:48
# @Author  : zxl
# @FileName: Baidu02_2.py






def solve(mat):

    m = len(mat)
    n = len(mat[0])


    newmat = []
    for i in range(n):
        newmat.append([0 for j in range(m)])

    for i in range(m):
        for j in range(n):
            newmat[j][m-1-i] = mat[i][j]


    return newmat


mat = [[1,2,3],
       [4,5,6]]
newmat = solve(mat)
print(newmat)







