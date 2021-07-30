# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 17:20
# @Author  : zxl
# @FileName: I0108.py


class Solution:
    def setZeroes(self, matrix ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        row0 = False
        col0 = False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0]==0:
                col0 = True
                break
        for j in range(n):
            if matrix[0][j]==0:
                row0 = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0



