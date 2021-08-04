# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 16:43
# @Author  : zxl
# @FileName: 074_4.py

class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:


        m = len(matrix)
        n = len(matrix[0])

        i = m-1
        j = 0
        while i>=0 and j<n:

            if target== matrix[i][j]:
                return True

            if target>matrix[i][j]:
                j+=1
            else:
                i-=1
        return False


