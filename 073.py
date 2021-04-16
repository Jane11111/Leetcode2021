# -*- coding: utf-8 -*-
# @Time    : 2021-03-21 15:49
# @Author  : zxl
# @FileName: 073.py


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        r_f = False
        c_f = False
        for i in range(m):
            if matrix[i][0] == 0:
                c_f = True
        for j in range(n):
            if matrix[0][j] == 0:
                r_f = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        f = True


        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if r_f:
            for j in range(n):
                matrix[0][j] = 0
        if c_f:
            for i in range(m):
                matrix[i][0] = 0

obj = Solution()
matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
obj.setZeroes(matrix)
print(matrix)

