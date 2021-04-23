# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:35
# @Author  : zxl
# @FileName: Offer004.py


class Solution:
    def findNumberIn2DArray(self, matrix , target ) :

        if len(matrix) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        i = m-1
        j = 0
        while i>=0 and j<n:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False