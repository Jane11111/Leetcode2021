# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 16:57
# @Author  : zxl
# @FileName: 378.py

class Solution:
    def kthSmallest(self, matrix , k: int) -> int:


        n = len(matrix)
        arr = [0 for i in range(n)]

        count = 0

        while count<k:
            count+=1


            min_val = float('inf')
            idx = -1
            for i in range(n):
                if arr[i]>=n:
                    continue
                if matrix[i][arr[i]]<min_val:
                    min_val = matrix[i][arr[i]]
                    idx = i
            arr[idx] += 1

            if count == k:
                return min_val








