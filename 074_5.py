# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 16:51
# @Author  : zxl
# @FileName: 074_5.py



class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        h = m*n-1


        while l<h:

            m = (l+h)//2

            i = m//n
            j = m%n

            if target<=matrix[i][j]:
                h = m
            else:
                l = m+1

        i = l//n
        j = l%n
        return matrix[i][j] == target
