# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 14:21
# @Author  : zxl
# @FileName: 074_2.py



class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:

        n = len(matrix[0])
        i = len(matrix)-1
        j = 0

        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i-=1
            else:
                j+=1
        return False