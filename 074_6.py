# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 17:46
# @Author  : zxl
# @FileName: 074_6.py


class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])


        l = 0
        h = m-1

        while l<h:
            m = (l+h+1)//2

            if matrix[m][0]>target:
                h = m-1
            else:
                l = m

        row = l
        l = 0
        h = n-1

        while l<h:
            m = (l+h)//2

            if target<=matrix[row][m]:
                h = m
            else:
                l = m+1
        return matrix[row][l] == target




