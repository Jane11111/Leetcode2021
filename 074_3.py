# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 18:41
# @Author  : zxl
# @FileName: 074_3.py



class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        i = m-1
        j = 0

        while i>=0 and j<n:

            if matrix[i][j] == target:
                return True

            if target>matrix[i][j]:
                j+=1
            else:
                i-=1
        return False