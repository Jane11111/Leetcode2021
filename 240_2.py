# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 20:05
# @Author  : zxl
# @FileName: 240_2.py


class Solution:
    def searchMatrix(self, matrix , target ) :


        m = len(matrix)
        n = len(matrix[0])

        i = m-1
        j = 0
        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False
