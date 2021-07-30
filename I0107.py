# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 17:10
# @Author  : zxl
# @FileName: I0107.py


class Solution:
    def rotate(self, mat ) -> None:



        n = len(mat)

        i = 0
        j = n-1
        while i<j:
            for k in range(n):
                mat[i][k],mat[j][k] = mat[j][k],mat[i][k]
            i+=1
            j-=1

        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
