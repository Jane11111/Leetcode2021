# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 14:06
# @Author  : zxl
# @FileName: 048_3.py




class Solution:
    def rotate(self, matrix ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        n = len(matrix)

        for i in range(n//2):

            e = n-i-1

            for j in range(i,e):

                matrix[i][j],matrix[j][e] , matrix[e][e-(j-i)], matrix[e-(j-i)][i] = matrix[e-(j-i)][i],matrix[i][j],matrix[j][e],matrix[e][e-(j-i)]

