# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 17:23
# @Author  : zxl
# @FileName: 048_2.py



class Solution:
    def rotate(self, matrix ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        n = len(matrix)
        s = 0
        e = n-1
        while s<e:
            for i in range(s,e):
                matrix[s][i],matrix[i][e],matrix[e][n-1-i],matrix[n-1-i][s] = matrix[n-1-i][s],matrix[s][i],matrix[i][e],matrix[e][n-1-i]
            s+=1
            e-=1