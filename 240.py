# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 19:50
# @Author  : zxl
# @FileName: 240.py


class Solution:
    def searchMatrix(self, matrix , target ) :

        m = len(matrix)
        n = len(matrix[0])

        min_row = m
        max_row = 0
        for i in range(m):
            if target>=matrix[i][0] and target <= matrix[i][n-1]:
                min_row= min(min_row,i)
                max_row = max(max_row,i)
        min_col = n
        max_col = 0
        for j in range(n):
            if target>=matrix[0][j] and target <= matrix[m-1][j]:
                min_col = min(min_col,j)
                max_col = max(max_col,j)

        for i in range(min_row,max_row+1):
            for j in range(min_col,max_col+1):
                if matrix[i][j] == target:
                    return True
        return False