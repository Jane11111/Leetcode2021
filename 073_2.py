# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 17:02
# @Author  : zxl
# @FileName: 073_2.py


class Solution:
    def setZeroes(self, matrix ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col0 = False
        row0 = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0

